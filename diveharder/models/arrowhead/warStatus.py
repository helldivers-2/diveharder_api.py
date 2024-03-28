from pydantic import BaseModel
from typing import List


class PlanetStatus(BaseModel):
    index: int
    owner: int
    health: int
    regenPerSecond: float
    players: int


class PlanetAttack(BaseModel):
    source: int
    target: int


class Campaign(BaseModel):
    id: int
    planetIndex: int
    type: int
    count: int


class JointOperation(BaseModel):
    id: int
    planetIndex: int
    hqNodeIndex: int


class PlanetEvent(BaseModel):
    id: int
    planetIndex: int
    eventType: int
    race: int
    health: int
    maxHealth: int
    startTime: int
    expireTime: int
    campaignId: int
    jointOperationIds: List[int]


class GlobalEvent(BaseModel):
    eventId: int
    title: str
    message: str
    race: int
    flag: int
    effectIds: List[int]
    planetIndices: List[int]


class WarStatus(BaseModel):
    warId: int
    time: int
    impactMultiplier: float
    storyBeatId32: int
    planetStatus: List[PlanetStatus]
    planetAttacks: List[PlanetAttack]
    campaigns: List[Campaign]
    communityTargets: list
    jointOperations: List[JointOperation]
    planetEvents: List[PlanetEvent]
    planetActiveEffects: list
    activeElectionPolicyEffects: list
    globalEvents: List[GlobalEvent]
    superEarthWarResults: list
