import streamlit as st
from PIL import Image
from src.utils import extract_text_from_image, is_dish, get_image_url

@st.dialog("📷 Uploaded Image")
def show_dialog_uploaded_image(image):
    st.image(image, caption="Uploaded Menu", use_container_width=True)

@st.dialog("✨ Curious, How it all comes together ?")
def show_dialog_help():
    st.header("📤 1. Upload Menu Image")
    st.subheader("Select an image from your gallery or capture one using your camera.")
    st.header("🧠 2. Extract Text with OCR")
    st.subheader("We use the powerful Tesseract engine to read and extract text from your menu.")
    st.header("🧪 3. Classify Dish Items")
    st.subheader("Our custom-trained model identifies which text entries are actual dishes.")
    st.header("🖼️ 4. Fetch Dish Images")
    st.subheader("We search multiple free image APIs to find matching images for each dish.")

def setup_layout():
    st.set_page_config(page_title="Menu Lens", layout="centered")
    st.title("🧿 Menu Lens")
    # Footer section layout
    # st.markdown("""
    # <style>
    #     .footer {
    #         position: fixed;
    #         left: 0;
    #         bottom: 0;
    #         width: 100%;
    #         text-align: center;
    #         padding: 10px;
    #         font-size: 0.9rem;
    #         color: gray;
    #         background-color: #f9f9f9;
    #     }
    # </style>
    # <div class="footer">
    #     🍽️ Made with ❤️ for food explorers | © 2025 Menu Lens
    # </div>
    # """, unsafe_allow_html=True)

def init():
    setup_layout()
    # if st.button("🤔 Curious, How it all comes together?"):
    #     show_dialog_help()
    image = None
    uploaded = st.file_uploader("Upload a menu image", type=["jpg", "jpeg", "png", "svg", "webp"])
    if uploaded:
        try:
            image = Image.open(uploaded)

            if image:
                l, uploaded_image_middle,r = st.columns([1, 2, 1])
                with uploaded_image_middle.popover("📸 See uploaded image", use_container_width=True):
                    st.image(image, caption=f"{uploaded.name}", use_container_width=True)

            if image:
                st.subheader("✨ Result")
                with st.spinner("Image analysis is in progress..."):
                    lines = extract_text_from_image(image)
                    dishes = [line for line in lines if is_dish(line)]
                    if dishes:
                        st.success(f"🌼 Found {len(dishes)} dish(es).")
                        cols = st.columns(3)
                        for i, dish in enumerate(dishes):
                            with cols[i % 3]:
                                image_url = get_image_url(dish)
                                if image_url:
                                    st.image(image_url, caption=dish, use_container_width=True)
                    else:
                        st.warning("🌼 No dishes found.")
                
            
        except Exception  as e:
            st.toast(f"🍂 Kaboom! That didn't go as planned. Error: {str(e)}")
            st.error(f"🍂 Kaboom! That didn't go as planned. Error: {str(e)}")
