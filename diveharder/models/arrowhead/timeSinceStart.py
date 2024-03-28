from pydantic import BaseModel


class TimeSinceStart(BaseModel):
    secondsSinceStart: int
