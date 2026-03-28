import pyfiglet
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from models.text_to_banner import TextToBanner

router = APIRouter()


@router.get("/")
async def root():
    return "Hello, world!"  # TODO: think of returning an html which has links to docs


@router.post("/text-to-banner", response_class=PlainTextResponse)
async def text_to_banner_endpoint(text_to_banner: TextToBanner):
    banner = pyfiglet.figlet_format(text_to_banner.prompt, font=text_to_banner.font)
    return f"Font: {text_to_banner.font}\n\n{banner}"
