import unicodedata as ud

from pydantic import BaseModel, model_validator

from services.font_utils import (
    CYRILLIC,
    CYRILLIC_DISPLAY,
    LATIN,
    LATIN_DISPLAY,
    all_available_fonts,
    get_cyrillic_fonts,
)

cyrillic_fonts = get_cyrillic_fonts()


class TextToBanner(BaseModel):
    prompt: str
    font: str = "standard"
    cyrillic: bool = False

    @model_validator(mode="after")
    def validate_font_prompt(
        self,
    ):  # TODO: create separate function for validating font and one for prompt
        valid_fonts = cyrillic_fonts if self.cyrillic else all_available_fonts
        if self.font not in valid_fonts:
            raise ValueError(
                f"Invalid font: {self.font}. Available {CYRILLIC_DISPLAY if self.cyrillic else ''} fonts: {valid_fonts}"
            )

        for char in self.prompt:
            if char.isspace():
                continue
            category = ud.category(char)
            if not category.startswith(("L", "N", "P", "S")):
                raise ValueError(
                    f"Invalid char: {char}. Only letters, digits, punctuation, symbols allowed."
                )
            if category.startswith("L"):
                expected_script = CYRILLIC if self.cyrillic else LATIN
                char_name = ud.name(char)
                if expected_script not in char_name:
                    raise ValueError(
                        f"Invalid char: {char}. "
                        f"Only {CYRILLIC_DISPLAY if self.cyrillic else LATIN_DISPLAY} letters allowed"
                    )
        return self
