# MenuLens
### site link:
- https://menu-lens.streamlit.app/
<p align="center">
  <img width="80%" alt="image" src="https://github.com/user-attachments/assets/d6ac62d2-da90-4060-875c-dd24b1eb7298" />  
</p>

### tech used:
- python
- streamlit: for ui
- tesseract, tesseract-ocr: for ocr
- classifer model: trained model on labeled data & exported as .pkl
- image api: serpi, duckduck-go
- deployment: streamlit
  
### project setup:
1. clone repo & create env
   - python -m venv .venv

2. activate it
    - for windows
        - .venv\Scripts\activate
    - for mac/linux
        - source .venv/bin/activate 

4. install libs
    - pip install -r requirements.txt

5. install tessaract
    - for windows install from github repo with lang. pack

    - for linux (Ubuntu / Debian)
        - sudo apt update
        - sudo apt install tesseract-ocr tesseract-ocr-mar tesseract-ocr-hin tesseract-ocr-eng tesseract-ocr-spa
        - tesseract -v

6. create env var
    - copy .env_template
    - remove _template
    - replace your keys

7. run app
    - streamlit run main.py
  

### improvements:
- add fallback way for rate limiter
- improve UI
- improve model tranning & classifier
- add models to github


