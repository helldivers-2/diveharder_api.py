from pydantic import BaseModel


class Campaign(BaseModel):
    id: int
    planetIndex: int
    type: int
    count: int
