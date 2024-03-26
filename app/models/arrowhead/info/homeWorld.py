from pydantic import BaseModel
from typing import List


class HomeWorld(BaseModel):
    race: int
    planetIndices: List[int]
