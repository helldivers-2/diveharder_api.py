from copy import deepcopy
from time import time, strftime, localtime
from re import sub

import aiohttp
import asyncio

from diveharder.utils.logging import logger, log, debug
import diveharder.data.cfg.constants as constants
import diveharder.data.cfg.settings as settings

BASE_URL = settings.api["BASE_URL"]
TIME_DELAY = int(settings.api["TIME_DELAY"])
TIMEOUT = int(settings.api["TIMEOUT"])

REQUEST_HEADERS = constants.api["REQUEST_HEADERS"]

urls = [
    settings.api["STATUS_API_URL"],
    settings.api["WARINFO_API_URL"],
    settings.api["PLANET_STATS_API_URL"],
    settings.api["MAJOR_ORDER_API_URL"],
    settings.api["NEWS_FEED_API_URL"],
    settings.api["WARID_API_URL"],
    settings.api["TIMESINCESTART_API_URL"],
    settings.api["NEWS_TICKER_API_URL"],
    settings.api["GALACTICE_WAR_EFFECTS_API_URL"],
    settings.api["LEVELSPEC_API_URL"],
    settings.api["ITEMS_API_URL"],
    settings.api["MISSION_REWARD_API_URL"],
    settings.api["HOTF_LEADERBOARD_API_URL"],
    settings.api["STEAM_NEWS_API_URL"],
]


class API:
    def __init__(self):
        # API Fetch and Cache Variables
        self.races = constants.faction["names"]
        self.planet_names = constants.planets["names"]
        self.sectors = constants.planets["sectors"]

        self.last_update_time = 0
        self.update_time = int(time())

        self.raw_data = {
            "status": [],
            "warinfo": [],
            "planetStats": [],
            "majorOrder": [],
            # "newsFeed": [],
            "warId": [],
            "timeSinceStart": [],
            "newsTicker": [],
            "galacticWarEffects": [],
            "levelSpec": [],
            "items": [],
            "missionRewards": [],
            "leaderboard": [],
            "updates": [],
        }

        self.all_data = {
            "status": [],
            "warinfo": [],
            "planetStats": [],
            "majorOrder": [],
            "newsFeed": [],
            "warId": [],
            "timeSinceStart": [],
            "newsTicker": [],
            "galacticWarEffects": [],
            "levelSpec": [],
            "items": [],
            "missionRewards": [],
            "leaderboard": [],
            "updates": [],
            "races": self.races,
            "planetNames": self.planet_names,
            "sectors": self.sectors,
        }

    async def time_check(self):
        new_time = int(time())
        debug(f"API | Time Check | {(new_time - self.update_time)}s")
        return self.update_time <= new_time - TIME_DELAY

    async def update(self, force: bool = False):
        debug("API | Update")
        time = await self.time_check()
        if time or force:
            responses = await self.request()
            await self.set_raw_all(responses)
            await self.format_data()

        return True

    async def request(self):
        responses = []
        request_urls = []
        for url in urls:
            if not url.startswith("http"):
                url = BASE_URL + url
            request_urls.append(url)
        tasks = [asyncio.create_task(self.get_url(url)) for url in request_urls]
        responses = await asyncio.gather(*tasks)
        return responses

    async def get_url(self, url: str = ""):
        headers = {"Accept-Language": "en-US"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                debug("URL: " + url)
                debug("Status: " + str(response.status))
                debug("Content-type: " + str(response.headers["content-type"]))
                return await response.json()

    async def set_raw_all(self, responses: list = []):
        self.raw_data["status"] = self.all_data["status"] = responses[0]
        self.raw_data["warinfo"] = self.all_data["warinfo"] = responses[1]
        self.raw_data["planetStats"] = self.all_data["planetStats"] = responses[2]
        self.raw_data["majorOrder"] = self.all_data["majorOrder"] = responses[3]
        self.raw_data["newsFeed"] = self.all_data["newsFeed"] = responses[4]
        self.raw_data["warId"] = self.all_data["warId"] = responses[5]
        self.raw_data["timeSinceStart"] = self.all_data["timeSinceStart"] = responses[6]
        self.raw_data["newsTicker"] = self.all_data["newsTicker"] = responses[7]
        self.raw_data["galacticWarEffects"] = self.all_data["galacticWarEffects"] = (
            responses[8]
        )
        self.raw_data["levelSpec"] = self.all_data["levelSpec"] = responses[9]
        self.raw_data["items"] = self.all_data["items"] = responses[10]
        self.raw_data["missionRewards"] = self.all_data["missionRewards"] = responses[
            11
        ]
        self.raw_data["leaderboard"] = self.all_data["leaderboard"] = responses[12]

        updates_pop_list = [
            "gid",
            "is_external_url",
            "feedname",
            "feedlabel",
            "feed_type",
            "tags",
            "appid",
            "author",
        ]
        for news in responses[13]["appnews"]["newsitems"]:
            for popper in updates_pop_list:
                if popper in news:
                    news.pop(popper)
            news["date"] = strftime("%d-%b-%Y %H:%M", localtime(news["date"]))
        self.raw_data["updates"] = self.all_data["updates"] = responses[13]["appnews"][
            "newsitems"
        ]

    async def format_data(self):
        return True
