from pydantic import BaseModel
from typing import List

from .info.homeWorld import HomeWorld
from .info.planetInfo import PlanetInfo


class WarInfo(BaseModel):
    warId: int
    startDate: int
    endDate: int
    minimumClientVersion: str
    planetInfos: List[PlanetInfo]
    homeWorlds: List[HomeWorld]
    # TODO: Capitals
    # TODO: planetPermEffectsgit her
