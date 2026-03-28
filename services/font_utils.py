import pyfiglet

CYRILLIC = "CYRILLIC"
LATIN = "LATIN"
CYRILLIC_DISPLAY = "Cyrillic"
LATIN_DISPLAY = "Latin"

all_available_fonts = pyfiglet.Figlet().getFonts()


def get_cyrillic_fonts():
    dummy_input = "Здравейте"
    working_fonts = []

    for font in all_available_fonts:
        dummy_output = pyfiglet.figlet_format(dummy_input, font=font)
        if dummy_output.strip():
            working_fonts.append(font)
    return working_fonts
