from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, model_validator
import pyfiglet
import unicodedata as ud


CYRILLIC = 'CYRILLIC'
LATIN = 'LATIN'
CYRILLIC_DISPLAY = "Cyrillic"
LATIN_DISPLAY = "Latin"
all_available_fonts = pyfiglet.Figlet().getFonts()
app = FastAPI()


def get_cyrillic_fonts():
	dummy_input = "Здравейте"
	working_fonts = []

	for font in all_available_fonts:
		dummy_output = pyfiglet.figlet_format(dummy_input, font=font)
		if dummy_output.strip():
			working_fonts.append(font)
	
	return working_fonts

cyrillic_fonts = get_cyrillic_fonts()


class TextToBanner(BaseModel):
	prompt: str
	font: str = pyfiglet.DEFAULT_FONT
	cyrillic: bool = False

	@model_validator(mode='after')
	def validate(self):

		# validate font
		valid_fonts = cyrillic_fonts if self.cyrillic else all_available_fonts
		if self.font not in valid_fonts:
			raise ValueError(f"Invalid font: {self.font}. The available {CYRILLIC_DISPLAY if self.cyrillic else ''} fonts are: {valid_fonts}")

		# validate prompt
		for char in self.prompt:
			if char.isspace():
				continue

			category = ud.category(char)

			if not category.startswith(('L', 'N', 'P', 'S')):
				raise ValueError(f"Invalid char: {char}. Category {category} found. Only letters, digits, punctuation, and symbols are allowed.")

			if category.startswith('L'):
				expected_script = CYRILLIC if self.cyrillic else LATIN
				char_name = ud.name(char)

				if expected_script not in char_name:
					script_type = CYRILLIC_DISPLAY if self.cyrillic else LATIN_DISPLAY
					raise ValueError(f"Invalid char: {char}. Only {script_type} letters allowed (along with digits, punctuation, and symbols)")

		return self


@app.post("/text-to-banner", response_class = PlainTextResponse)
async def text_to_banner(text_to_banner: TextToBanner):
	banner = pyfiglet.figlet_format(text_to_banner.prompt, font=text_to_banner.font)
	return f"Font: {text_to_banner.font}\n\n{banner}"