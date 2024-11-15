# --- STANDARD LIBRARIES --- #
from time import strftime, localtime
from typing import List

# --- FASTAPI IMPORTS --- #
from fastapi import APIRouter, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

# --- DH APP IMPORTS --- #
from src.data.api import handler
import src.utils.log as log
from src.data.json_handler import json_data, helper_data

# --- RESPONSE MODELS --- #
from src.routes.response_models.status import StatusResponse
from src.routes.response_models.war_info import WarInfoResponse
from src.routes.response_models.planet_stats import PlanetStatsResponse
from src.routes.response_models.major_order import MajorOrderResponse
from src.routes.response_models.news_feed import NewsFeedResponse
from src.routes.response_models.updates import UpdateResponse
from src.routes.response_models.war_id import WarIdResponse
from src.routes.response_models.items import ItemsResponse

router = APIRouter(prefix="/v1", tags=["v1"], include_in_schema=True)

api = handler.api


@router.get("/all")
async def get_all(request: Request):
    """
    All AHGS API Calls + Formatted Versions provided by me

    Note: Updates from Steam News are parsed from BBCode to Markdown.

    Any AHGS Authenticated API Endpoints may be unreliable at this time.

    - We are looking into making them more reliable but until we can generate
      the proper authentication we have to rely on rednecked solutions.

    """
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    return data


@router.get("/status")
async def get_v1_status(request: Request) -> StatusResponse:
    """Get the v1 data for status"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("status", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/war_info")
async def get_v1_war_info(request: Request) -> WarInfoResponse:
    """Get the v1 data for war_info"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("war_info", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/planet_stats")
async def get_v1_planet_stats(request: Request) -> PlanetStatsResponse:
    """Get the v1 data for planet_stats"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("planet_stats", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/major_order")
async def get_v1_major_order(request: Request) -> List[MajorOrderResponse]:
    """Get the v1 data for major_order"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("major_order", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/personal_order")
async def get_v1_major_order(request: Request) -> List[MajorOrderResponse]:
    """Get the v1 data for personal_order"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("personal_order", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/news_feed")
async def get_v1_news_feed(request: Request) -> List[NewsFeedResponse]:
    """Get the v1 data for news_feed"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("news_feed", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/updates")
async def get_v1_updates(request: Request) -> List[UpdateResponse]:
    """Get the v1 data for updates"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("updates", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/war_id")
async def get_v1_war_id(request: Request) -> WarIdResponse:
    """Get the v1 data for war_id"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("war_id", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/items")
async def get_v1_items(request: Request) -> ItemsResponse:
    """Get the v1 data for items"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("items", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/store_rotation")
async def get_v1_store_rotation(request: Request):
    """Get the v1 data for store_rotation"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("store_rotation", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/election_candidates")
async def get_v1_election_candidates(request: Request):
    """Get the v1 data for election_candidates"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("election_candidates", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/election_policies")
async def get_v1_election_policies(request: Request):
    """Get the v1 data for election_policies"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("election_policies", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/minigame_leaderboard")
async def get_v1_minigame_leaderboard(request: Request):
    """Get the v1 data for minigame_leaderboard"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("minigame_leaderboard", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/player_leaderboard")
async def get_v1_player_leaderboard(request: Request):
    """Get the v1 data for player_leaderboard"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("player_leaderboard", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/commend_leaderboard")
async def get_v1_commend_leaderboard(request: Request):
    """Get the v1 data for commend_leaderboard"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("commend_leaderboard", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/clan_leaderboard")
async def get_v1_clan_leaderboard(request: Request):
    """Get the v1 data for clan_leaderboard"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("clan_leaderboard", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/planets")
async def get_v1_planets(request: Request):
    """Get the v1 data for planets"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("planets", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/warbonds")
async def get_v1_warbonds(request: Request):
    """Get the v1 data for warbonds"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("warbonds", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/factions")
async def get_v1_factions(request: Request):
    """Get the v1 data for factions"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("factions", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/mission_rewards")
async def get_v1_mission_rewards(request: Request):
    """Get the v1 data for mission_rewards"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("mission_rewards", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/level_spec")
async def get_v1_level_spec(request: Request):
    """Get the v1 data for level_spec"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("level_spec", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/score_calc")
async def get_v1_score_calc(request: Request):
    """Get the v1 data for score_calc"""
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    response = data.get("score_calc", [])
    if response:
        return response
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


async def update_data():
    no_include = [
        "mission_rewards",
        "level_spec",
        "score_calc",
        "season_pass",
        "season_pass_hm",
        "season_pass_sv",
        "season_pass_ce",
        "season_pass_dd",
        "season_pass_pp",
        "season_pass_vc",
        "season_pass_ff",
        "season_pass_ca",
        "season_pass_te",
        "space_station_1"
    ]
    data = {
        k: v["data"]
        for k, v in api.raw_data.items()
        if v["data"] and k not in no_include
    }
    data.update(json_data)
    data["store_rotation"] = await update_store_data(data.get("store_rotation", {}))
    data["player_leaderboard"] = data.get("player_leaderboard", {}).get("entries", [])
    data["commend_leaderboard"] = data.get("commend_leaderboard", {}).get("entries", [])
    return data


def get_buy_price_amount(item_id=None):
    super_item = []

    for item in api.raw_data.get("items", {}).get("data", {}):
        if str(item.get("itemId")) == item_id or str(item.get("mixId")) == item_id:
            super_item = item
            break

    if "buyPrice" in super_item and len(super_item["buyPrice"]) > 0:
        return super_item.get("buyPrice", [{}])[0].get(
            "amount", 0
        )  # Assuming only one buy price
    else:
        log.msg("buyPrice Not Found")
        return None  # No buy price available


async def update_store_data(data):
    expire_time = strftime("%d-%b-%Y %H:%M", localtime(int(data.get("expireTime", 0))))

    raw_store_items = [
        str(item["mixId"])
        for item in data.get("salesPage", {}).get("sections", [{}])[0].get("items", {})
    ]
    store_items = []
    for k, v in helper_data["item_list"].items():
        if (
            v["mix_id"] not in raw_store_items and k not in raw_store_items
        ):  # or (v["mix_id"] in store_items or k in store_items):
            continue
        elif v["mix_id"] in raw_store_items or k in raw_store_items:
            if k in json_data["items"]["armor"]:
                store_items.append(k)

    items = []
    for item in store_items:
        if "Unmapped" in item:
            continue
        if item in json_data["items"]["armor"]:
            item_data = json_data["items"]["armor"][item]
            item_data.update({"store_cost": get_buy_price_amount(item)})
            items.append(item_data)
        else:
            items.append({"name": f"Unmapped: {item}"})
    if not items:
        items: List[dict[str, str]] = [
            {"name": "Unmapped: NO STORE DATA"},
            {"name": "Unmapped: NO STORE DATA"},
            {"name": "Unmapped: NO STORE DATA"},
            {"name": "Unmapped: NO STORE DATA"},
        ]
    return {"expire_time": expire_time, "items": items}
