from copy import deepcopy
from time import time, strftime, localtime
from re import sub

import grequests

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
    settings.api["NEWS_TICKER_API_URL"],
    settings.api["NEWS_FEED_API_URL"],
    settings.api["TIMESINCESTART_API_URL"],
    settings.api["WARID_API_URL"],
    settings.api["GALACTICE_WAR_EFFECTS_API_URL"],
    settings.api["LEVELSPEC_API_URL"],
    settings.api["ITEMS_API_URL"],
    settings.api["MISSION_REWARD_API_URL"],
    settings.api["MAJOR_ORDER_API_URL"],
    settings.api["HOTF_LEADERBOARD_API_URL"],
    settings.api["STEAM_NEWS_API_URL"],
]


class API:
    def __init__(self):
        # API Fetch and Cache Variables
        self.status_response = []
        self.warinfo_response = []
        self.planet_stats_response = []
        self.news_ticker_response = []
        self.news_feed_response = []
        self.timesincestart_response = []
        self.warid_response = []
        self.galactic_war_effects_response = []
        self.levelspec_response = []
        self.leaderboard_response = []
        self.items_api_response = []
        self.mission_reward_response = []
        self.major_order_response = []
        self.steam_news_response = []

        self.last_status_response = []
        self.last_warinfo_response = []
        self.last_planet_stats_response = []
        self.last_news_ticker_response = []
        self.last_news_feed_response = []
        self.last_timesincestart_response = []
        self.last_warid_response = []
        self.last_galactic_war_effects_response = []
        self.last_levelspec_response = []
        self.last_leaderboard_response = []
        self.last_items_api_response = []
        self.last_mission_reward_response = []
        self.last_major_order_response = []
        self.last_steam_news_response = []

        self.all_raw_responses = {}
        self.all_responses = {}
        self.races = {1: "Humans", 2: "Terminids", 3: "Automatons", 4: "Illuminate"}
        self.planet_names = constants.planets["names"]
        self.sectors = constants.planets["sectors"]

        self.last_update_time = 0
        self.update_time = int(time())

    # API Fetch and Cache Methods

    def time_check(self):
        new_time = int(time())
        debug(f"API | Time Check | {(new_time - self.update_time)}s")
        return self.update_time <= new_time - TIME_DELAY

    async def update(self, force: bool = False):
        debug("API | Update")
        if self.time_check() or force:
            self.last_update_time = self.update_time
            self.update_time = int(time())
            await self.cache(initial=False)
            response = await self.send_requests()
            await self.assign_responses(response)
            self.all_raw_responses = {
                "status": self.status_response,
                "warinfo": self.warinfo_response,
                "planetStats": self.planet_stats_response,
                "majorOrder": self.major_order_response,
                "newsFeed": self.news_feed_response,
                "warId": self.warid_response,
                "timeSinceStart": self.timesincestart_response,
                "newsTicker": self.news_ticker_response,
                "galacticWarEffects": self.galactic_war_effects_response,
                "levelSpec": self.levelspec_response,
                "items": self.items_api_response,
                "missionRewards": self.mission_reward_response,
                "leaderboard": self.leaderboard_response,
                "updates": self.steam_news_response,
            }
            custom_all = {
                "races": self.races,
                "planetNames": self.planet_names,
                "sectors": self.sectors,
            }
            self.all_responses = self.all_raw_responses | custom_all

            debug("--- API | Update | Caching Start ---")
            await self.cache(initial=True)
            debug("--- API | Update | Done ---")
        else:
            debug("--- API | Update | Not Needed ---")

    async def send_requests(self):
        debug("API | Send Requests")
        url_requests = (
            (
                grequests.get(url, headers=REQUEST_HEADERS)
                if url.startswith("https://")
                else grequests.get(BASE_URL + url, headers=REQUEST_HEADERS)
            )
            for url in urls
        )
        response_list = grequests.map(url_requests)

        return response_list

    async def assign_responses(self, response_list):
        debug("API | Assign Responses")
        self.status_response = response_list[0].json()
        self.warinfo_response = response_list[1].json()
        self.planet_stats_response = response_list[2].json()
        self.news_ticker_response = response_list[3].json()
        self.news_feed_response = response_list[4].json()
        self.timesincestart_response = response_list[5].json()
        self.warid_response = response_list[6].json()
        self.galactic_war_effects_response = response_list[7].json()
        self.levelspec_response = response_list[8].json()
        self.items_api_response = response_list[9].json()
        self.mission_reward_response = response_list[10].json()
        self.major_order_response = response_list[11].json()
        self.leaderboard_response = response_list[12].json()
        self.steam_news_response = response_list[13].json()["appnews"]["newsitems"]
        pops = [
            "gid",
            "is_external_url",
            "feedname",
            "feedlabel",
            "feed_type",
            "tags",
            "appid",
            "author",
        ]
        for news in self.steam_news_response:
            for popper in pops:
                if popper in news:
                    news.pop(popper)
            news["date"] = strftime("%d-%b-%Y %H:%M", localtime(news["date"]))
            news["contents"] = sub(r"\[img\](.*?)\[/img\]", "", news["contents"])
            news["contents"] = sub(
                r"\[previewyoutube=(.*?);full\]\[/previewyoutube\]",
                "",
                news["contents"],
            )
            news["contents"] = sub(r"\[h2\](.*?)\[/h2\]", r"## \1", news["contents"])
            news["contents"] = sub(r"\[b\](.*?)\[/b\]", r"**\1**", news["contents"])
            news["contents"] = sub(r"\[list\]", r"\n", news["contents"])
            news["contents"] = sub(r"\[/list\]", r"\n", news["contents"])
            news["contents"] = sub(r"\[\*\]", "- ", news["contents"])
            news["contents"] = sub(r"\[i\](.*?)\[/i\]", r"*\1*", news["contents"])
            news["contents"] = sub(r"\n\n", r"\n", news["contents"])
            news["contents"] = sub(r"\n\n", r"\n", news["contents"])
            news["contents"] = sub(r"\n\n", r"\n", news["contents"])
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r" . ", ". ", news["contents"])

        return True

    async def cache(self, initial: bool = False):
        debug("API | Cache")
        if not initial and self.status_response:
            # Cache API data before fetching new data.
            debug("--- API | Update | Caching ---")
            self.last_status_response = (
                deepcopy(self.status_response) if self.status_response else []
            )
            self.last_warinfo_response = (
                deepcopy(self.warinfo_response) if self.warinfo_response else []
            )
            self.last_planet_stats_response = (
                deepcopy(self.planet_stats_response)
                if self.planet_stats_response
                else []
            )
            self.last_news_ticker_response = (
                deepcopy(self.news_ticker_response) if self.news_ticker_response else []
            )
            self.last_news_feed_response = (
                deepcopy(self.news_feed_response) if self.news_feed_response else []
            )
            self.last_timesincestart_response = (
                deepcopy(self.timesincestart_response)
                if self.timesincestart_response
                else []
            )
            self.last_warid_response = (
                deepcopy(self.warid_response) if self.warid_response else []
            )
            self.last_galactic_war_effects_response = (
                deepcopy(self.galactic_war_effects_response)
                if self.galactic_war_effects_response
                else []
            )
            self.last_levelspec_response = (
                deepcopy(self.levelspec_response) if self.levelspec_response else []
            )
            self.last_leaderboard_response = (
                deepcopy(self.leaderboard_response) if self.leaderboard_response else []
            )
            self.last_items_api_response = (
                deepcopy(self.items_api_response) if self.items_api_response else []
            )
            self.last_mission_reward_response = (
                deepcopy(self.mission_reward_response)
                if self.mission_reward_response
                else []
            )
            self.last_major_order_response = (
                deepcopy(self.major_order_response) if self.major_order_response else []
            )
            self.last_steam_news_response = (
                deepcopy(self.steam_news_response) if self.steam_news_response else []
            )

        elif initial and not self.last_status_response:
            # We only cache API data AFTER requests if this is the first run of this boot.
            debug("--- API | Update | Initial Cache  ---")
            self.last_status_response = (
                deepcopy(self.status_response) if not self.last_status_response else []
            )
            self.last_warinfo_response = (
                deepcopy(self.warinfo_response)
                if not self.last_warinfo_response
                else []
            )
            self.last_planet_stats_response = (
                deepcopy(self.planet_stats_response)
                if not self.last_planet_stats_response
                else []
            )
            self.last_news_ticker_response = (
                deepcopy(self.news_ticker_response)
                if not self.last_news_ticker_response
                else []
            )
            self.last_news_feed_response = (
                deepcopy(self.news_feed_response)
                if not self.last_news_feed_response
                else []
            )
            self.last_timesincestart_response = (
                deepcopy(self.timesincestart_response)
                if not self.last_timesincestart_response
                else []
            )
            self.last_warid_response = (
                deepcopy(self.warid_response) if not self.last_warid_response else []
            )
            self.last_galactic_war_effects_response = (
                deepcopy(self.galactic_war_effects_response)
                if not self.last_galactic_war_effects_response
                else []
            )
            self.last_levelspec_response = (
                deepcopy(self.levelspec_response)
                if not self.last_levelspec_response
                else []
            )
            self.last_leaderboard_response = (
                deepcopy(self.leaderboard_response)
                if not self.last_leaderboard_response
                else []
            )
            self.last_items_api_response = (
                deepcopy(self.items_api_response)
                if not self.last_items_api_response
                else []
            )
            self.last_mission_reward_response = (
                deepcopy(self.mission_reward_response)
                if not self.last_mission_reward_response
                else []
            )
            self.last_major_order_response = (
                deepcopy(self.major_order_response)
                if not self.last_major_order_response
                else []
            )
            self.last_steam_news_response = (
                deepcopy(self.steam_news_response)
                if not self.last_steam_news_response
                else []
            )
        else:
            return True
        return True
