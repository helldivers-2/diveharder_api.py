import asyncio
from re import sub
from time import time, strftime, localtime

import aiohttp

import src.cfg.settings as cfg
import src.utils.log as log


class API:
    def __init__(self):
        self.races = {}
        self.planet_data = {}
        self.items = {}

        self.request_headers = cfg.ahgs_api.get("request_headers")
        self.auth_headers = cfg.ahgs_api.get("auth_headers")

        self.urls = cfg.urls

        self.update_time = 0
        self.time_delay: int = cfg.ahgs_api.get("time_delay", 20)

        self.raw_data = {
            "status": {"data": [], "update_time": 0, "auth": True},
            "war_info": {"data": [], "update_time": 0, "auth": True},
            "planet_stats": {"data": [], "update_time": 0, "auth": True},
            "major_order": {"data": [], "update_time": 0, "auth": True},
            "personal_order": {"data": [], "update_time": 0, "auth": True},
            "news_feed": {"data": [], "update_time": 0, "auth": True},
            "updates": {"data": [], "update_time": 0, "auth": False},
            "level_spec": {"data": [], "update_time": 0, "auth": True},
            "war_id": {"data": {"id": cfg.war_id}, "update_time": 0, "auth": True},
            "items": {"data": [], "update_time": 0, "auth": True},
            "mission_rewards": {"data": [], "update_time": 0, "auth": True},
            "store_rotation": {"data": [], "update_time": 0, "auth": True},
            "season_pass": {"data": [], "update_time": 0, "auth": True},
            "season_pass_hm": {"data": [], "update_time": 0, "auth": True},
            "season_pass_sv": {"data": [], "update_time": 0, "auth": True},
            "season_pass_ce": {"data": [], "update_time": 0, "auth": True},
            "season_pass_dd": {"data": [], "update_time": 0, "auth": True},
            "season_pass_pp": {"data": [], "update_time": 0, "auth": True},
            "season_pass_vc": {"data": [], "update_time": 0, "auth": True},
            "season_pass_ff": {"data": [], "update_time": 0, "auth": True},
            "season_pass_ca": {"data": [], "update_time": 0, "auth": True},
            "season_pass_te": {"data": [], "update_time": 0, "auth": True},
            "space_station_1": {"data": [], "update_time": 0, "auth": False},
            "score_calc": {"data": [], "update_time": 0, "auth": True},
            "election_candidates": {"data": [], "update_time": 0, "auth": True},
            "election_terms": {"data": [], "update_time": 0, "auth": True},
            "election_policies": {"data": [], "update_time": 0, "auth": True},
            "minigame_leaderboard": {"data": [], "update_time": 0, "auth": True},
            "player_leaderboard": {"data": [], "update_time": 0, "auth": False},
            "commend_leaderboard": {"data": [], "update_time": 0, "auth": True},
            "clan_leaderboard": {"data": [], "update_time": 0, "auth": True},
        }

    async def time_check(self, update_time: int = 0):
        log.debug("API | Time Check")
        current_time = int(time())
        time_diff = current_time - update_time
        log.debug(f"API | Time Check | {time_diff} seconds")
        return time_diff > self.time_delay

    async def update_all(self):
        log.debug("API | Update All")
        responses = await self.fetch_all()
        update_needed = await self.time_check(update_time=self.update_time)
        if update_needed:
            # Update Needed
            for i, (key, value) in enumerate(self.raw_data.items()):
                self.raw_data[key]["data"] = responses[i]
                self.raw_data[key]["update_time"] = int(time())
                if key == "updates":
                    if not isinstance(self.raw_data[key]["data"], list):
                        # If pulling from steam, we gotta format, otherwise you're probably using my shit, so it's already formatted
                        # and we just leave it alone
                        self.raw_data[key]["data"] = await self.format_steam_news(
                            self.raw_data[key]["data"]["appnews"]["newsitems"]
                        )
            self.update_time = int(time())

    async def fetch_all(self):
        log.debug(f"API | Fetching All Data")
        request_urls = []
        is_authed = []
        for i, (k, v) in enumerate(self.raw_data.items()):
            request_urls.append(self.urls[k])
            is_authed.append(v["auth"])
        tasks = [
            asyncio.create_task(self.get_url(url, auth))
            for (url, auth) in zip(request_urls, is_authed)
        ]
        responses = await asyncio.gather(*tasks)
        return responses

    async def fetch_data(self, info_name: str = ""):
        log.debug(f"API | Fetching {info_name} Data")

        update_needed = await self.time_check(
            update_time=self.raw_data.get(info_name, {"bool": False}).get(
                "update_time", int(time())
            )
        )
        if update_needed:
            authed = self.raw_data.get(info_name, {})["auth"]
            url = self.urls[info_name]
            self.raw_data[info_name]["update_time"] = int(time())
            self.raw_data[info_name]["data"] = await self.get_url(url, authed)
            if info_name == "updates":
                self.raw_data[info_name]["data"] = await self.format_steam_news(
                    self.raw_data[info_name]["data"]["appnews"]["newsitems"]
                )

    async def get_url(self, url: str, auth: bool):
        log.debug("API | Getting URL")
        headers = self.auth_headers if auth else self.request_headers
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                content_type = resp.headers.get("Content-Type", "No Content Type")
                if "json" in content_type:
                    payload = await resp.json()
                else:
                    payload = {}
                return payload

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
            news["date"] = strftime("%d-%b-%Y %H:%M", localtime(int(news["date"])))

            # Handle Non-Formatting Steam Markdown
            news["contents"] = sub(
                r"\[previewyoutube=(.+);full]\[/previewyoutube]",
                "[YouTube](https://www.youtube.com/watch?v=" + r"\1)",
                news["contents"],
            )
            news["contents"] = sub(r"\[img](.*?\..{3,4})\[/img]", "", news["contents"])

            news["contents"] = news["contents"].replace("\n  \n", "\n")
            news["contents"] = news["contents"].replace("\n\n\n\n", "\n")
            news["contents"] = news["contents"].replace("\n\n\n\n", "\n")
            news["contents"] = news["contents"].replace("\n\n\n", "\n")
            news["contents"] = news["contents"].replace("\n\n", "\n")

            # Handle Formatting Steam Markdown
            news["contents"] = sub(r"\[h1](.*?)\[/h1]", r"\n# \1", news["contents"])
            news["contents"] = sub(r"\[h2](.*?)\[/h2]", r"\n## \1", news["contents"])
            news["contents"] = sub(r"\[h3](.*?)\[/h3]", r"\n### \1", news["contents"])
            news["contents"] = sub(r"\[h4](.*?)\[/h4]", r"\n#### \1", news["contents"])
            news["contents"] = sub(r"\[h5](.*?)\[/h5]", r"\n##### \1", news["contents"])
            news["contents"] = sub(
                r"\[h6](.*?)\[/h6]", r"\n###### \1", news["contents"]
            )
            news["contents"] = sub(
                r"\[url=(.+?)](.+?)\[/url]", r"[\2]\(\1\)", news["contents"]
            )
            news["contents"] = sub(
                r"\[quote](.+?)\[/quote]]", r"\n> \1\n", news["contents"]
            )
            news["contents"] = sub(r"\[b](.+?)\[/b]", r"\n**\1**", news["contents"])
            news["contents"] = sub(r"\[i](.+?)\[/i]", r"*\1*", news["contents"])
            news["contents"] = sub(r"\[u](.+?)\[/u]", r"\n__\1__", news["contents"])
            news["contents"] = sub(r"\[list]", r"", news["contents"])
            news["contents"] = sub(r"\[/list]", r"", news["contents"])
            news["contents"] = sub(r"\[\*]", r"- ", news["contents"])
            news["contents"] = news["contents"].replace("\n\n", "\n")
        return all_news
