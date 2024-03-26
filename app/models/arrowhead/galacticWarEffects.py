from pydantic import BaseModel
from typing import List


class GalacticWarEffect(BaseModel):
    id: int
    effectType: int
    nameHash: int
    descriptionFluffHash: int
    descriptionGamePlayLongHash: int
    descriptionGamePlayShortHash: int
    valueTypes: List[int]
    values: List[int]


class GalacticWarEffects(BaseModel):
    galacticWarEffects: List[GalacticWarEffect]
