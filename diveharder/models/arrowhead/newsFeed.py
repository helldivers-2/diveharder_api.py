from pydantic import BaseModel
from typing import List


class NewsFeedItem(BaseModel):
    id: int
    published: int
    type: int
    message: str
