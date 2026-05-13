import pyfiglet

from constants import WEIRD_FONTS

CYRILLIC = "CYRILLIC"
LATIN = "LATIN"
CYRILLIC_DISPLAY = "Cyrillic"
LATIN_DISPLAY = "Latin"

all_fonts = [font for font in pyfiglet.Figlet().getFonts() if font not in WEIRD_FONTS]


def get_cyrillic_fonts():
    dummy_input = "Здравейте"
    working_fonts = []

    for font in all_fonts:
        dummy_output = pyfiglet.figlet_format(dummy_input, font=font)
        if dummy_output.strip():
            working_fonts.append(font)
    return working_fonts


cyrillic_fonts = get_cyrillic_fonts()
