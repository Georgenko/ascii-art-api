from io import BytesIO
from urllib.parse import quote

import httpx
from PIL import Image

from constants import POLLINATIONS_URL
from models.promp_to_image import PromptToImageRequest


async def generate_image_from_prompt(prompt: str) -> Image.Image:
    url = POLLINATIONS_URL.format(prompt=quote(prompt))
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.get(url)
        response.raise_for_status()
    return Image.open(BytesIO(response.content))


async def convert_prompt_to_image(request: PromptToImageRequest) -> str:
    image = await generate_image_from_prompt(request.prompt)
    image.save("temp.png")
