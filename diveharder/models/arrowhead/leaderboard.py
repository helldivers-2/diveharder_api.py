from pydantic import BaseModel
from typing import List


class Leader(BaseModel):
    experience: int
    banner: int
    name: str
    isSelf: bool
    score: int
    rank: int


class Leaderboard(BaseModel):
    pageNumber: int
    pageSize: int
    totalRecords: int
    entries: List[Leader]


class Error(BaseModel):
    errorCode: int
    traceId: str
    message: str
