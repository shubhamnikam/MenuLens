import pytesseract
from PIL import Image
import pickle
import requests
from serpapi import GoogleSearch
import os
from duckduckgo_search import DDGS
import time
import streamlit as st


def setup_header():
    with st.popover("🧿 Menu Lens", use_container_width=True):

        st.text("✨ Curious, How it all comes together ?")
        st.code(f"""
📤 1. Upload Menu Image: Select an image from your gallery or capture one using your camera.
🧠 2. Extract Text with OCR: We use the powerful Tesseract engine to read and extract text from your menu.
🧪 3. Classify Dish Items: Our custom-trained classifier model identifies which text entries are actual dishes.
🖼️ 4. Fetch Dish Images: We search multiple free image APIs to find matching images for each dish.
""")

        st.text("👻 About")
        a1, a2, a3 = st.columns([3, 2, 4])
        a1.link_button("🧬 Github - MenuLense",
                       "https://github.com/shubhamnikam/MenuLens", use_container_width=True)
        a2.link_button(
            "👨‍💻 Dev Profile", "https://linktr.ee/shubhamnikam", use_container_width=True)
        a3.link_button("❤️ github/shubhamnikam",
                       "https://github.com/shubhamnikam", use_container_width=True)

        st.text("📌 Note (Made with ❤️ for food explorers 🍽️)")
        st.code(f"""  
1. This is a free-time weekend project, so don’t expect it to work like magic.
2. I'm using only FOSS (Free and Open Source Software) libraries. As a result, you may encounter the following limitations:
    - Rate limiting by the image API
    - Inaccurate or limited image results
    - No support for languages other than English
3. To avoid rate limit exceptions from the image API
    - I've deliberately added a 2–3 second delay.
    - which may make the app feel slow.
4. Possible improvements:
    - The classifier model requires fine-tuning
    - Additional free image APIs can be added as fallback options.
5. No Support for other languages
    - Text extraction is supported, but the model is not trained to handle other languages.
""")


def show_input_info(uploaded, image, ocr_lines, classified_dishes):

    uploaded_image_col, debug_info_col = st.columns([3, 1])

    with uploaded_image_col.popover("📸 See uploaded image", use_container_width=True):
        st.image(image, caption=f"{uploaded.name}", use_container_width=True)

    with debug_info_col.popover("🔭 Debug info", use_container_width=True):
        if ocr_lines:
            st.subheader("📃 Extracted text:")
            st.code("\n".join(ocr_lines))

        if classified_dishes:
            st.subheader("🩺 Classified dishes:")
            st.code("\n".join(classified_dishes))



with open("./src/models/v2/dish_classifier.pkl", "rb") as f:
    model = pickle.load(f)


def extract_text_from_image(image: Image.Image) -> list[str]:
    lang_code = "eng+hin+mar+tam+tel+ben+fra+ara+spa+chi_sim"
    tesseract_cmd_path = os.getenv("TESSERACT_CMD_PATH")
    if tesseract_cmd_path:
        pytesseract.pytesseract.tesseract_cmd = rf"{tesseract_cmd_path}"
    text = pytesseract.image_to_string(image, lang=lang_code)
    return [line.strip() for line in text.split("\n") if line.strip()]


def is_dish(text: str) -> bool:
    return model.predict([text])[0] == 'dish'


def get_image_url(query: str) -> str:
    # explicit sleep
    time.sleep(3)
    if False:
        return setup_serp_api(query)
    elif True:
        return setup_duckduckgo_api(query)


def setup_duckduckgo_api(query: str) -> str:
    results = DDGS().images(
        keywords=query,
        region="us-en",
        safesearch="moderate",
        size=None,
        color=None,
        type_image=None,
        layout=None,
        license_image=None,
        max_results=1,
    )
    if results:
        return results[0]["image"]
    return None



def setup_serp_api(query: str) -> str:
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        raise ValueError("SERPAPI_KEY not found in environment variables.")
    params = {
        "q": query,
        "tbm": "isch",
        "api_key": api_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    images = results.get("images_results", [])
    print(results)
    if images[0]["thumbnail"]:
        return images[0]["thumbnail"]
    else:
        return None