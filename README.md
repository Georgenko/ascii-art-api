# ASCII Art API

Generate ASCII art from text, images, or prompts using FastAPI

## 🚀 **Live demo:** [ascii-art-api-c9a7.onrender.com](https://ascii-art-api-c9a7.onrender.com)

## Description
A fun side project built to learn FastAPI. It exposes three ways to generate ASCII art:
convert a text string into a styled banner, transform an uploaded image into its ASCII
equivalent, or describe something in a prompt and let it generate + convert the image for you.

## Endpoints:
 - **text-to-banner**: converts a text string into an ASCII art banner
 - **image-to-image**: converts an uploaded image into ASCII art
 - **prompt-to-image**: generates an image from a text prompt, then converts it to ASCII art

## Project structure
```
├── main.py          # App entry point
├── endpoints.py     # Route definitions
├── constants.py     # Shared static values
├── models/          # Pydantic request models
├── services/        # Business logic
├── static/          # JS + CSS
├── templates/       # HTML
└── tests/
```

## Run locally
```
git clone https://github.com/Georgenko/ascii-art-api.git
cd ascii-art-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
