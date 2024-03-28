from pydantic import BaseModel
from typing import List


class NewsTickerItem(BaseModel):
    id32: int
    context: int
    group: int


class NewsTicker(BaseModel):
    messages: List[NewsTickerItem]
