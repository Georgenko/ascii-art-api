from pathlib import Path

BASE_DIR = Path(__file__).parent

TEMPLATES_DIR = BASE_DIR / "templates"
INDEX_HTML = TEMPLATES_DIR / "index.html"

DEFAULT_WIDTH = 128
MAX_WIDTH = 10_000  # just to have a limitation
STD_CHAR_RAMP = (
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
)
DEFAULT_NUM_CHARS = len(STD_CHAR_RAMP)
MINIMAL_CHAR_RAMP = "@#S%?*+;:,. "
IHDR_BYTES_LENGTH = 25

POLLINATIONS_URL = "https://image.pollinations.ai/prompt/{prompt}"
