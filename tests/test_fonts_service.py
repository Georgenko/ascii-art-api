from services.fonts import all_fonts, cyrillic_fonts


def test_fonts_not_empty():
    assert len(cyrillic_fonts) > 0
    assert len(all_fonts) > 0
