from pydantic import BaseModel
from typing import List


class PlanetCoordinates(BaseModel):
    x: float
    y: float


class PlanetInfo(BaseModel):
    index: int
    settingsHash: int
    position: PlanetCoordinates
    waypoints: List[int]
    sector: int
    maxHealth: int
    disabled: bool
    initialOwner: int


class HomeWorld(BaseModel):
    race: int
    planetIndices: List[int]


class WarInfo(BaseModel):
    warId: int
    startDate: int
    endDate: int
    minimumClientVersion: str
    planetInfos: List[PlanetInfo]
    homeWorlds: List[HomeWorld]
    capitalInfos: list
    planetPermanentEffects: list
