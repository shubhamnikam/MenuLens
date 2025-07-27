import pytesseract
from PIL import Image
import pickle
import requests
from serpapi import GoogleSearch
import os
from duckduckgo_search import DDGS
import time

with open("./src/models/v1/dish_classifier.pkl", "rb") as f:
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
    # explicit sleep
    time.sleep(1)
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