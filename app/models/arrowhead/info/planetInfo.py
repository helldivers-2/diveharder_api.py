from pydantic import BaseModel
from typing import List
from .planetCoordinates import PlanetCoordinates


class PlanetInfo(BaseModel):
    index: int
    settingsHash: int
    position: PlanetCoordinates
    waypoints: List[int]
    sector: int
    maxHealth: int
    disabled: bool
    initialOwner: int
