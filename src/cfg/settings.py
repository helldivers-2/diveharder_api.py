import os
from urllib.parse import unquote

import requests
from dotenv import load_dotenv

if os.path.isfile("./src/cfg/env/.env"):
    load_dotenv("./src/cfg/env/.env")


security = {
    "token": os.environ["SECURITY_TOKEN"],
}

ahgs_api = {
    "request_headers": {
        "Accept-Language": "en-US",
        "User-Agent": "Diveharder API - api.diverharder.com",
    },
    "auth_headers": {
        "Accept-Language": "en-US",
        "User-Agent": "Diveharder API - api.diverharder.com",
        "Authorization": os.environ["SESSION_TOKEN"],
    },
    "time_delay": 20,
}


base_url = os.environ["BASE_URL"]

war_id_url = base_url + os.environ["WAR_ID"]
war_id_json = requests.get(war_id_url).json()
war_id = war_id_json["id"]

urls = {
    "status": base_url + os.environ["STATUS"],
    "war_info": base_url + os.environ["WAR_INFO"],
    "war_id": war_id_url,
    "planet_stats": base_url + os.environ["PLANET_STATS"],
    "major_order": base_url + os.environ["MAJOR_ORDER"],
    "news_feed": base_url + os.environ["NEWS_FEED"],
    "updates": os.environ["STEAM_NEWS"],
    "level_spec": base_url + os.environ["LEVEL_SPEC"],
    "items": base_url + os.environ["ITEMS"],
    "mission_rewards": base_url + os.environ["MISSION_REWARDS"],
    "store_rotation": base_url + os.environ["STORE_ROTATION"],
    "season_pass": base_url + os.environ["SEASON_PASS"],
    "season_pass_hm": base_url + os.environ["SEASON_PASS_HM"],
    "season_pass_sv": base_url + os.environ["SEASON_PASS_SV"],
    "season_pass_ce": base_url + os.environ["SEASON_PASS_CE"],
    "season_pass_dd": base_url + os.environ["SEASON_PASS_DD"],
    "score_calc": base_url + os.environ["MISSION_SCORE_CALC_PARAMS"],
    "election_candidates": base_url + os.environ["ELECTION_CANDIDATES"],
    "election_terms": base_url + os.environ["ELECTION_TERMS"],
    "election_policies": base_url + os.environ["ELECTION_POLICIES"],
    "minigame_leaderboard": base_url + os.environ["MINIGAME_LEADERBOARD"],
    "player_leaderboard": base_url + os.environ["PLAYER_LEADERBOARD"],
    "commend_leaderboard": base_url + os.environ["COMMEND_LEADERBOARD"],
    "clan_leaderboard": base_url + os.environ["CLAN_LEADERBOARD"],
}

for i, (key, value) in enumerate(urls.items()):
    urls[key] = unquote(value)
    if "%id" in value:
        urls[key] = urls[key].replace("%id", str(war_id))
