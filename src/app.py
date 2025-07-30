import streamlit as st
from PIL import Image
from src.utils import extract_text_from_image, is_dish, get_image_url, show_input_info, setup_header

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

                    show_input_info(uploaded, image, ocr_lines, classified_dishes)

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
