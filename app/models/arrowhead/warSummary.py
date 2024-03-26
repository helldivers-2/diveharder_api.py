from pydantic import BaseModel
from typing import List


class GalaxyStats(BaseModel):
    missionsWon: int
    missionsLost: int
    missionTime: int
    bugKills: int
    automatonKills: int
    illuminateKills: int
    bulletsFired: int
    bulletsHit: int
    timePlayed: int
    deaths: int
    revives: int
    friendlies: int
    missionSuccessRate: int
    accurracy: int


class PlanetStats(BaseModel):
    planetIndex: int
    missionsWon: int
    missionsLost: int
    missionTime: int
    bugKills: int
    automatonKills: int
    illuminateKills: int
    bulletsFired: int
    bulletsHit: int
    timePlayed: int
    deaths: int
    revives: int
    friendlies: int
    missionSuccessRate: int
    accurracy: int


class WarSummary(BaseModel):
    galaxy_stats: GalaxyStats
    planets_stats: List[PlanetStats]
