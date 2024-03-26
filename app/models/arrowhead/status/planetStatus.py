from pydantic import BaseModel


class PlanetStatus(BaseModel):
    index: int
    owner: int
    health: int
    regenPerSecond: float
    players: int
