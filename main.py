from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
import pyfiglet

class TextToBanner(BaseModel):
	prompt: str
	font: str | None = None

app = FastAPI()

@app.post("/text-to-banner", response_class=PlainTextResponse)
async def text_to_banner(text_to_banner: TextToBanner):
	# TODO: add validation for fonts, if they are not one of the supported for pyfiglet, it crashes
	f = pyfiglet.figlet_format(text_to_banner.prompt, font=text_to_banner.font)
	return f