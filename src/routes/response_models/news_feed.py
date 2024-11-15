from pydantic import BaseModel
from typing import List, Any


class NewsFeedResponse(BaseModel):
    id: int
    published: int
    type: int
    tagIds: List[Any]
    message: str
