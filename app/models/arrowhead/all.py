from pydantic import BaseModel
from typing import List

from .warStatus import WarStatus
from .warInfo import WarInfo
from .warSummary import WarSummary
from .warId import WarID
from .newsFeed import NewsFeedItem
from .assignment import Assignment
from .timeSinceStart import TimeSinceStart
from .levelspec import Level
from .newsticker import NewsTicker
from .galacticWarEffects import GalacticWarEffect
from .missionrewards import MissionRewards
from .item import Item


class AllRaw(BaseModel):
    status: WarStatus
    warinfo: WarInfo
    planetStats: WarSummary
    majorOrder: List[Assignment]
    newsFeed: List[NewsFeedItem]
    warId: WarID
    timeSinceStart: TimeSinceStart
    newsTicker: NewsTicker
    galacticWarEffects: List[GalacticWarEffect]
    levelSpec: List[Level]
    items: List[Item]
    missionRewards: MissionRewards
