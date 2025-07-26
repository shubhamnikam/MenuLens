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
```cmd
## create project
mkdir menu-lens-py
cd menu-lens-py

# create env
python -m venv .venv

# for windows
.venv\Scripts\activate

# for mac/linux
source .venv/bin/activate 

# install
create requirements.txt & add libs
pip install -r requirements.txt

# create app
- get file
- extract text
- pass it to model for classification
- get images
```

