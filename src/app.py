import streamlit as st
from PIL import Image
from src.utils import extract_text_from_image, is_dish, get_image_url


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

        st.text("📌 Note ")
        st.code(f"""  
1. I'm trying to use only FOSS (Free and Open Source Software) libraries and apps to achieve this.
2. To avoid rate limit exceptions from the image API
    - I've deliberately added a 2–3 second delay.
    - which may make the app feel slow.
3. The app can be improved in the following ways:
    - The classifier model needs fine-tuning.
    - Additional free image APIs can be added as fallback options.
4. Made with ❤️ for food explorers 🍽️  
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


def init():
    setup_header()
    image = None
    uploaded = st.file_uploader("Upload a menu image", type=[
                                "jpg", "jpeg", "png", "svg", "webp"])
    if uploaded:
        try:
            image = Image.open(uploaded)
            if image:
                with st.spinner("Image analysis is in progress..."):
                    ocr_lines = extract_text_from_image(image)

                    classified_dishes = [
                        line for line in ocr_lines if is_dish(line)]

                    show_input_info(uploaded, image, ocr_lines,
                                    classified_dishes)

                    if classified_dishes:
                        st.success(
                            f"🌼 Result: Found {len(classified_dishes)} dish(es).")
                        cols = st.columns(3)
                        for i, dish in enumerate(classified_dishes):
                            with cols[i % 3]:
                                image_url = get_image_url(dish)
                                if image_url:
                                    st.image(image_url, caption=dish,
                                             use_container_width=True)
                    else:
                        st.warning("🌼 Result: No dishes found.")

        except Exception as e:
            st.toast(f"🍂 Glitch in the matrix. Error: {str(e)}")
            st.error(f"🍂 Glitch in the matrix. Error: {str(e)}")
