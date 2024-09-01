from pydantic import BaseModel
from typing import List


class Campaign(BaseModel):
    id: int
    planetIndex: int
    type: int
    count: int


class PlanetAttack(BaseModel):
    source: int
    target: int


class PlanetStatus(BaseModel):
    index: int
    owner: int
    health: int
    regenPerSecond: float
    players: int


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
    id32: int
    portraitId32: int
    title: str
    titleId32: int
    message: str
    messageId32: int
    race: int
    flag: int
    assignmentId32: int
    effectIds: List[int] | None
    planetIndices: List[int] | None


class PlanetActiveEffects(BaseModel):
    index: int
    galacticEffectId: int


class StatusResponse(BaseModel):
    warId: int
    time: int
    impactMultiplier: float
    storyBeatId32: int
    planetStatus: List[PlanetStatus]
    planetAttacks: List[PlanetAttack]
    campaigns: List[Campaign]
    communityTargets: List[int] | None
    jointOperations: List[JointOperation]
    planetEvents: List[PlanetEvent]
    planetActiveEffects: List[PlanetActiveEffects] | None
    activeElectionPolicyEffects: List[int] | None
    globalEvents: list[GlobalEvent]
    superEarthWarResults: List[int] | None
    layoutVersion: int
