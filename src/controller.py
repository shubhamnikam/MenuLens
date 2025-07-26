import streamlit as st
from PIL import Image
from src.utils import extract_text_from_image, is_dish, get_image_url

def init():
    st.set_page_config(page_title="Menu Lens", layout="centered")
    st.title("🧿 Menu Lens")

    option = st.radio("Choose input method", ("Upload from file", "Capture from camera"))

    image = None

    if option == "Upload from file":
        uploaded = st.file_uploader("Upload a menu image", type=["jpg", "jpeg", "png", "svg", "webp"])
        if uploaded:
            image = Image.open(uploaded)

    elif option == "Capture from camera":
        captured = st.camera_input("Take a photo")
        if captured:
            image = Image.open(captured)

    if image:
        with st.spinner("Analyzing..."):
            lines = extract_text_from_image(image)
            dishes = [line for line in lines if is_dish(line)]

        
        st.subheader("✨ Result")
        if dishes:
            st.success(f"Found {len(dishes)} dish(es).")
            cols = st.columns(3)
            for i, dish in enumerate(dishes):
                with cols[i % 3]:
                    st.image(get_image_url(dish), caption=dish, use_container_width =True)
        else:
            st.warning("No dishes found.")

        st.subheader("📷 Uploaded Image")
        st.image(image, caption="Uploaded Menu", use_container_width =True)