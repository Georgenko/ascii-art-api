from typing import Annotated

from fastapi import APIRouter, Query, UploadFile
from fastapi.responses import HTMLResponse, PlainTextResponse

from constants import DEFAULT_NUM_CHARS, DEFAULT_WIDTH, INDEX_HTML, MAX_WIDTH
from models.promp_to_image import PromptToImageRequest
from models.text_to_banner import TextToBannerRequest
from services.banner import convert_text_to_banner
from services.fonts import (
    all_fonts,
    cyrillic_fonts,
)
from services.image import convert_image_to_image, validate_image
from services.prompt import convert_prompt_to_image

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def root():
    return INDEX_HTML.read_text()


@router.get("/fonts")
async def get_fonts(cyrillic: bool = False):
    if cyrillic:
        return f"All cyrillic fonts are: {cyrillic_fonts}"
    return f"All fonts are: {all_fonts}"
    # TODO instead of returning only the font names you can return a sample text with all fonts


@router.post("/text-to-banner", response_class=PlainTextResponse)
async def text_to_banner(request: TextToBannerRequest):
    return convert_text_to_banner(request)


@router.post("/image-to-image", response_class=PlainTextResponse)
async def image_to_image(
    image: UploadFile,
    width: Annotated[int, Query(gt=0, le=MAX_WIDTH)] = DEFAULT_WIDTH,
    num_chars: Annotated[int, Query(gt=0, le=DEFAULT_NUM_CHARS)] = DEFAULT_NUM_CHARS,
    minimal: bool = False,
):
    validate_image(image)
    return convert_image_to_image(image, width, num_chars, minimal)


@router.post("/prompt-to-image", response_class=PlainTextResponse)
async def prompt_to_image(request: PromptToImageRequest):
    return await convert_prompt_to_image(request)
