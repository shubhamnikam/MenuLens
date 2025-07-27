# MenuLens

## Phase 1
1. Click or Upload from file
2. OCR to extract text
3. Menu Images for extracted text
4. Deploy - add docker support & deploy 

## Phase 2
1. Add Url sharing to see menu
    1. Move logic to Backend & NoSQL DB
    2. Use Firestore DB
2. Change deployment

## Phase 3
1. Add User Auth
2. History


# create project - py
1. create project
    mkdir menu-lens-py
    cd menu-lens-py

2. create env
    python -m venv .venv

3. activate it
    - for windows
        .venv\Scripts\activate
    - for mac/linux
        source .venv/bin/activate 

4. install
- create requirements.txt & add libs
    pip install -r requirements.txt

5. install tessaract
    - for windows install from github repo

    - for linux (Ubuntu / Debian)
    sudo apt update
    sudo apt install tesseract-ocr
    sudo apt install tesseract-ocr-mar tesseract-ocr-hin

    tesseract -v

6. create env var
    - copy .env_template
    - remove _template
    - replace your keys

7. create app
    - get file
    - extract text
    - pass it to model for classification
    - get images

