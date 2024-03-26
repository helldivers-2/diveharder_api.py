from pydantic import BaseModel
from typing import List


class NewsFeedItem(BaseModel):
    id: int
    published: int
    type: int
    tagIds: List[int]
    message: str


class NewsFeed(BaseModel):
    news: List[NewsFeedItem]
