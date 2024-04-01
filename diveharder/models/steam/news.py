from pydantic import BaseModel
from typing import List


class NewsItem(BaseModel):
    title: str
    url: str
    contents: str
    date: str
