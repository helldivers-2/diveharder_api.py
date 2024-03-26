from pydantic import BaseModel


class PlanetAttack(BaseModel):
    source: int
    target: int
