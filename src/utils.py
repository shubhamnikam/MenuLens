import pytesseract
from PIL import Image
import pickle
import requests
from serpapi import GoogleSearch
import os

with open("./src/models/dish_classifier.pkl", "rb") as f:
    model = pickle.load(f)


def extract_text_from_image(image: Image.Image) -> list[str]:
    tesseract_cmd_path = os.getenv("TESSERACT_CMD_PATH")
    if tesseract_cmd_path:
        pytesseract.pytesseract.tesseract_cmd = rf"{tesseract_cmd_path}"
    text = pytesseract.image_to_string(image)
    return [line.strip() for line in text.split("\n") if line.strip()]


def is_dish(text: str) -> bool:
    return model.predict([text])[0] == 'dish'


def get_image_url(query: str) -> str:
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
