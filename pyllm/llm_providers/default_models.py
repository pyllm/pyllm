from pydantic import BaseModel


class DefaultModel(BaseModel):
    user_prompt: str
    response: str
    flags: list[str]
