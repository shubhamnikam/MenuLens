# MenuLens
### site link:
- https://menu-lens.streamlit.app/

### tech used:
- python
- streamlit: for ui
- tesseract, tesseract-ocr: for ocr
- classifer model: trained model on labeled data & exported as .pkl
- image api: serpi, duckduck-go
- deployment: streamlit
  
### project setup:
1. create project
   - mkdir menu-lens-py
   - cd menu-lens-py

2. create env
   - python -m venv .venv

3. activate it
    - for windows
        - .venv\Scripts\activate
    - for mac/linux
        - source .venv/bin/activate 

4. install
    - create requirements.txt & add libs
        - pip install -r requirements.txt

5. install tessaract
    - for windows install from github repo

    - for linux (Ubuntu / Debian)
        - sudo apt update
        - sudo apt install tesseract-ocr tesseract-ocr-mar tesseract-ocr-hin
        - tesseract -v

6. create env var
    - copy .env_template
    - remove _template
    - replace your keys

7. run app
    - streamlit run main.py
  

### improvements:
- add backup way for rate limiter
- improve UI
- improve model tranning & classifier
- add models to github


