from pydantic import BaseModel


class PlanetCoordinates(BaseModel):
    x: float
    y: float
