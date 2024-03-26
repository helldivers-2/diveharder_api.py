from pydantic import BaseModel
from typing import List


class Price(BaseModel):
    mixId: int
    amount: int
    flags: int


class Item(BaseModel):
    itemId: int
    mixId: int
    isConsumable: bool
    requiredLevel: int
    progressionCategory: int
    tags: List[int]
    requiredItems: List[int]
    buyPrice: List[Price]
    sellPrice: List[Price]
