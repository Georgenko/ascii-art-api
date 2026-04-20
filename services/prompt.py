import os
import unicodedata
from io import BytesIO
from urllib.parse import quote

import httpx
from PIL import Image

from constants import FILESYSTEM_UNSAFE_CHARS, POLLINATIONS_URL, SEPARATORS
from models.promp_to_image import PromptToImageRequest
from services.image import _pil_image_to_ascii


async def convert_prompt_to_image(request: PromptToImageRequest) -> str:
    image = await generate_image_from_prompt(request.prompt)

    filename = f"debug/{sanitize_filename(request.prompt)}"
    save_debug_img(image, filename)

    return _pil_image_to_ascii(
        image, request.width, request.num_chars, request.minimal, filename
    )


async def generate_image_from_prompt(prompt: str) -> Image.Image:
    url = POLLINATIONS_URL.format(prompt=quote(prompt))
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.get(url)
        response.raise_for_status()
    return Image.open(BytesIO(response.content))


def sanitize_filename(prompt: str, max_length: int = 150) -> str:
    text = unicodedata.normalize("NFKD", prompt)
    text = text.encode("ascii", "ignore").decode("ascii")  # keep only ascii
    text = FILESYSTEM_UNSAFE_CHARS.sub("_", text)
    text = SEPARATORS.sub("_", text)
    text = text.strip("_.")
    text = text[:max_length].strip("_.")
    return text or "unnamed.png"


def save_debug_img(image: Image.Image, filename: str) -> None:
    if not os.getenv("DEBUG", "false").lower() == "true":
        return
    image.save(fp=f"{filename}.png")
