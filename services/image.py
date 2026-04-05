from fastapi import HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError
from PIL.Image import Resampling

from constants import MINIMAL_CHAR_RAMP, STD_CHAR_RAMP


def validate_image(image: UploadFile):
    try:
        img = Image.open(image.file)
        img.verify()
        image.file.seek(0)
    except UnidentifiedImageError:
        raise HTTPException(
            status_code=400, detail="Image cannot be opened or identified"
        )
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Image is not valid: {ex.args}")


def convert_image_to_image(
    image: UploadFile, width_pixels: int, num_chars: int, minimal
) -> str:
    img = Image.open(image.file)
    return _pil_image_to_ascii(img, width_pixels, num_chars, minimal)


def _pil_image_to_ascii(
    img: Image.Image, width_pixels: int, num_chars: int, minimal: bool
) -> str:
    height_pixels = (
        width_pixels // 2
    )  # Because characters are twice as tall as they are wide
    img = img.resize((width_pixels, height_pixels), resample=Resampling.LANCZOS)

    # TODO: maybe explore using luma 709 and/or increasing contrast before converting
    img = img.convert("L")

    chars = MINIMAL_CHAR_RAMP if minimal else get_chars(num_chars)

    result = ""  # TODO: move to separate method
    pixels = list(img.getdata())
    for y in range(img.height):
        for x in range(img.width):
            pxl = pixels[y * img.width + x]
            result += chars[pxl * (len(chars) - 1) // 255]
        result += "\n"

    return result


def get_chars(n: int) -> str:
    step = len(STD_CHAR_RAMP) // n
    return STD_CHAR_RAMP[::step][:n]
