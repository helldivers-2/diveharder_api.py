from pydantic import BaseModel
from typing import List


class Reward(BaseModel):
    mixId: int
    amount: int


class Badge(BaseModel):
    id32: int
    amount: int
    influence: int
    itemRewards: List[Reward]


class Multiplier(BaseModel):
    id32: int
    factor: float
    influenceFactor: float


class MissionRewards(BaseModel):
    badges: List[Badge]
    multipliers: List[Multiplier]
