from pydantic import BaseModel
from typing import List


class Level(BaseModel):
    level: int
    requiredExperience: int


class LevelSpec(BaseModel):
    levels: List[Level]
