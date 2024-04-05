from copy import deepcopy
from time import time, strftime, localtime
from re import sub

import aiohttp
import asyncio

from diveharder.utils.logging import logger, log, debug
import diveharder.cfg.constants as constants
import diveharder.cfg.settings as settings

TIME_DELAY = int(settings.TIME_DELAY)
TIMEOUT = int(settings.TIMEOUT)

REQUEST_HEADERS = constants.api["REQUEST_HEADERS"]
AUTH_REQUEST_HEADERS = constants.api["AUTH_REQUEST_HEADERS"]

unauth_urls = settings.urls["unauth"]

auth_urls = settings.urls["auth"]


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
            unauth_responses = await self.request()
            auth_responses = await self.request_auth()
            await self.set_raw_all(unauth_responses, auth_responses)
            await self.format_data()

        return True

    async def request(self, headers: dict = REQUEST_HEADERS):
        responses = []
        request_urls = []

        for url in unauth_urls:
            request_urls.append(url)
        tasks = [
            asyncio.create_task(self.get_url(url, headers=headers))
            for url in request_urls
        ]
        responses = await asyncio.gather(*tasks)
        return responses

    async def request_auth(self, local_auth_urls: list = auth_urls):
        auth_responses = []
        auth_request_urls = []

        for url in local_auth_urls:
            auth_request_urls.append(url)
        tasks = [asyncio.create_task(self.get_url(url)) for url in auth_request_urls]
        auth_responses = await asyncio.gather(*tasks)
        return auth_responses

    async def get_url(self, url: str, headers: dict = AUTH_REQUEST_HEADERS):
        debug(headers)
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                debug("URL: " + url)
                debug("Status: " + str(response.status))
                content_type = response.headers.get("content-type", "No Content Type")
                debug("Content-type: " + str(content_type))
                payload = None
                if not content_type == "No Content Type" and content_type.startswith(
                    "application/json"
                ):
                    payload = await response.json()
                else:
                    payload = await response.text()

                return payload

    async def set_raw_all(self, responses: list = [], auth_responses: list = []):
        self.raw_data["status"] = self.all_data["status"] = auth_responses[0]
        self.raw_data["warinfo"] = self.all_data["warinfo"] = auth_responses[1]
        self.raw_data["planetStats"] = self.all_data["planetStats"] = auth_responses[2]
        self.raw_data["majorOrder"] = self.all_data["majorOrder"] = auth_responses[3]
        self.raw_data["newsFeed"] = self.all_data["newsFeed"] = auth_responses[4]
        self.raw_data["warId"] = self.all_data["warId"] = auth_responses[5]
        self.raw_data["timeSinceStart"] = self.all_data["timeSinceStart"] = (
            auth_responses[6]
        )
        self.raw_data["newsTicker"] = self.all_data["newsTicker"] = auth_responses[7]
        self.raw_data["galacticWarEffects"] = self.all_data["galacticWarEffects"] = (
            auth_responses[8]
        )
        self.raw_data["levelSpec"] = self.all_data["levelSpec"] = auth_responses[9]
        self.raw_data["items"] = self.all_data["items"] = auth_responses[10]
        self.raw_data["missionRewards"] = self.all_data["missionRewards"] = (
            auth_responses[11]
        )
        self.raw_data["leaderboard"] = self.all_data["leaderboard"] = responses[0]
        self.raw_data["updates"] = self.all_data["updates"] = (
            await self.format_steam_news(responses[1]["appnews"]["newsitems"])
        )
        self.raw_data["store_rotation"] = self.all_data["store_rotation"] = (
            auth_responses[12]
        )

    async def format_steam_news(self, all_news):
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
        for news in all_news:
            for popper in updates_pop_list:
                if popper in news:
                    news.pop(popper)
            news["date"] = strftime("%d-%b-%Y %H:%M", localtime(news["date"]))

            # Whitespace Handling
            news["contents"] = sub(r"\n ", r"\n", news["contents"])
            news["contents"] = sub(r" \n", r"\n", news["contents"])
            news["contents"] = sub(r"\n\n", r"\n", news["contents"])
            news["contents"] = sub(r"\n\n", r"\n", news["contents"])
            news["contents"] = sub(r"\n\n", r"\n", news["contents"])
            news["contents"] = sub(r"\n\n", r"\n", news["contents"])
            news["contents"] = sub(r"\n\n", r"\n", news["contents"])
            news["contents"] = sub(r"\n\n", r"\n", news["contents"])

            # Handle Formatting Steam Markdown
            news["contents"] = sub(
                r"\[h1\](.*?)\[/h1\]", r"\n\n# \1\n\n", news["contents"]
            )
            news["contents"] = sub(
                r"\[h2\](.*?)\[/h2\]", r"\n\n## \1\n\n", news["contents"]
            )
            news["contents"] = sub(
                r"\[h3\](.*?)\[/h3\]", r"\n\n### \1\n\n", news["contents"]
            )
            news["contents"] = sub(
                r"\[h3\](.*?)\[/h4\]", r"\n\n#### \1\n\n", news["contents"]
            )
            news["contents"] = sub(
                r"\[h3\](.*?)\[/h5\]", r"\n\n##### \1\n\n", news["contents"]
            )
            news["contents"] = sub(
                r"\[h3\](.*?)\[/h6\]", r"\n\n###### \1\n\n", news["contents"]
            )
            news["contents"] = sub(
                r"\[url=(.+?)](.+?)\[/url\]", r"[\2]\(\1\)", news["contents"]
            )

            news["contents"] = sub(r"\[quote\]", r"\n\n> ", news["contents"])
            news["contents"] = sub(r"\[quote\]", r"\n\n> ", news["contents"])
            news["contents"] = sub(r"\[/quote\]", r"\n\n", news["contents"])
            news["contents"] = sub(r"\[b\]", r"\n**", news["contents"])
            news["contents"] = sub(r"\[/b\]", r"**", news["contents"])
            news["contents"] = sub(r"\[i\]", r"*", news["contents"])
            news["contents"] = sub(r"\[/i\]", r"*", news["contents"])
            news["contents"] = sub(r"\[u\]", r"\n\n__", news["contents"])
            news["contents"] = sub(r"\[/u\]", r"__", news["contents"])
            news["contents"] = sub(r"\[list\]", r"\n", news["contents"])
            news["contents"] = sub(r"\[/list\]", r"\n", news["contents"])
            news["contents"] = sub(r"\[\*\]", r"  \n- ", news["contents"])

            # Handle Double Spaces
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r"  ", " ", news["contents"])
            news["contents"] = sub(r"\\n \\n", r"\n\n", news["contents"])
            news["contents"] = sub(r"\\n\\n\\n", r"\\n\\n", news["contents"])
            news["contents"] = sub(r"\\n\\n\\n", r"\\n\\n", news["contents"])
            news["contents"] = sub(r"\\n\\n\\n", r"\\n\\n", news["contents"])

            # Handle Non-Formatting Steam Markdown
            news["contents"] = sub(
                r"\[previewyoutube=(.+);full\]\[/previewyoutube\]",
                "[YouTube](https://www.youtube.com/watch?v=" + r"\1)",
                news["contents"],
            )
            news["contents"] = sub(r"\[img\].*?\..{3,4}\[/img\]", "", news["contents"])

        return all_news

    async def format_data(self):
        return True
