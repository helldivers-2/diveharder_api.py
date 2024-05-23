from pydantic import BaseModel
from typing import List, Any


class PlanetCoords(BaseModel):
    x: int
    y: int


class PlanetInfo(BaseModel):
    index: int
    settingsHash: int
    position: PlanetCoords
    waypoints: List[int]
    sector: int
    maxHealth: int
    disabled: bool
    initialOwner: int


class homeWorld(BaseModel):
    race: int
    planetIndices: List[int]


class WarInfoResponse(BaseModel):
    warId: int
    startDate: int
    endDate: int
    layoutVersion: int
    minimumClientVersion: str
    planetInfos: List[PlanetInfo]
    homeWorlds: List[homeWorld]
    capitalInfos: Any
    planetPermanentEffects: Any
