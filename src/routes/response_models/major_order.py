from pydantic import BaseModel
from typing import List, Optional



class Task(BaseModel):
    type: int
    values: List[int]
    valueTypes: List[int]


class Reward(BaseModel):
    type: int
    id32: int
    amount: int


class Setting(BaseModel):
    type: int
    overrideTitle: str
    overrideBrief: str
    taskDescription: str
    tasks: List[Task]
    reward: Optional[Reward] = None
    rewards: Optional[List[Reward]] = []
    flags: int


class MajorOrderResponse(BaseModel):
    id32: int
    progress: List[int]
    expiresIn: int
    setting: Setting
