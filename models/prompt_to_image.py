from pydantic import BaseModel, Field

from constants import DEFAULT_NUM_CHARS, DEFAULT_WIDTH, MAX_WIDTH


class PromptToImageRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=500)
    width: int = Field(default=DEFAULT_WIDTH, gt=0, le=MAX_WIDTH)
    num_chars: int = Field(default=DEFAULT_NUM_CHARS, gt=0, le=DEFAULT_NUM_CHARS)
    minimal: bool = False
