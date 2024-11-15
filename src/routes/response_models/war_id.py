from pydantic import BaseModel


class WarIdResponse(BaseModel):
    id: int
