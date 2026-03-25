from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, AfterValidator
from typing import Annotated
import pyfiglet

available_fonts = pyfiglet.Figlet().getFonts()

def check_valid_font(font: str):
	if font not in available_fonts:
		raise ValueError(f"Invalid font: {font}. Here is the list of supported ones: {available_fonts}")
	return font

class TextToBanner(BaseModel):
	prompt: str
	font: Annotated[str, AfterValidator(check_valid_font)] = pyfiglet.DEFAULT_FONT

app = FastAPI()

@app.post("/text-to-banner", response_class = PlainTextResponse)
async def text_to_banner(text_to_banner: TextToBanner):
	# TODO: add validation for prompt text as well (no cyrillic, maybe length and so on)
	f = pyfiglet.figlet_format(text_to_banner.prompt, font=text_to_banner.font)
	return f