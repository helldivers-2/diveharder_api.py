from pydantic import BaseModel
from typing import List, Any


class UpdateResponse(BaseModel):
    title: str
    url: str
    contents: str
    date: str
