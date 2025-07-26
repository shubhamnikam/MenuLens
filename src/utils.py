import pytesseract
from PIL import Image
import pickle
import requests

# Load the trained model
with open("./src/models/dish_classifier.pkl", "rb") as f:
    model = pickle.load(f)

def extract_text_from_image(image: Image.Image) -> list[str]:
    # pytesseract.pytesseract.tesseract_cmd = r"C:\Users\snikam\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(image)
    return [line.strip() for line in text.split("\n") if line.strip()]

def is_dish(text: str) -> bool:
    return model.predict([text])[0] == 'dish'

def get_image_url(dish: str) -> str:
    return f"https://source.unsplash.com/400x300/?{dish.replace(' ', '+')}"
