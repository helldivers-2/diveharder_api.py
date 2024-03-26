from .status.campaign import Campaign
from .status.planetAttack import PlanetAttack
from .status.planetStatus import PlanetStatus

from pydantic import BaseModel
from typing import List


class WarStatus(BaseModel):
    warId: int
    time: int
    impactMultiplier: float
    storyBeatId32: int
    planetStatus: List[PlanetStatus]
    planetAttacks: List[PlanetAttack]
    campaigns: List[Campaign]
