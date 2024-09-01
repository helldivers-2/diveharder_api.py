from fastapi import APIRouter, status
from fastapi.requests import Request
from starlette.responses import JSONResponse

from src.data.api import handler
import src.utils.log as log

api = handler.api

router = APIRouter(
    prefix="/raw",
    tags=["raw"],
    responses={404: {"description": "Not found"}},
)


@router.get("/all", status_code=200)
async def get_all_raw(request: Request):
    """
    All AHGS API Calls Only

    Note: Updates from Steam News are parsed from BBCode to Markdown.

    Any AHGS Authenticated API Endpoints may be unreliable at this time.

    - We are looking into making them more reliable but until we can generate
      the proper authentication we have to rely on rednecked solutions.

    """
    await api.update_all()
    no_include = [
        "items",
        "store_rotation",
        "mission_rewards",
        "level_spec",
        "score_calc",
        "season_pass",
        "season_pass_hm",
        "season_pass_sv",
        "season_pass_ce",
        "season_pass_dd",
        "season_pass_pp",
        "minigame_leaderboard",
        "player_leaderboard",
        "commend_leaderboard",
        "election_policies",
        "election_candidates",
    ]
    data = {}
    for k, v in api.raw_data.items():
        if v["data"] and k not in no_include:
            data[k] = v["data"]
    log.info(request, status.HTTP_200_OK)
    return data


@router.get("/status", status_code=200)
async def get_raw_status(request: Request):
    """Get the raw data for status"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="status")
    data = api.raw_data.get("status", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/war_info", status_code=200)
async def get_raw_war_info(request: Request):
    """Get the raw data for war_info"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="war_info")
    data = api.raw_data.get("war_info", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/planetstats", include_in_schema=False)
@router.get("/planet_stats", status_code=200)
async def get_raw_planet_stats(request: Request):
    """Get the raw data for planet_stats"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="planet_stats")
    data = api.raw_data.get("planet_stats", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/major_order", status_code=200)
async def get_raw_major_order(request: Request):
    """Get the raw data for major_order"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="major_order")
    data = api.raw_data.get("major_order", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/personal_order", status_code=200)
async def get_raw_personal_order(request: Request):
    """Get the raw data for personal_order"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="personal_order")
    data = api.raw_data.get("personal_order", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/news_feed", status_code=200)
async def get_raw_news_feed(request: Request):
    """Get the raw data for news_feed"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="news_feed")
    data = api.raw_data.get("news_feed", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/updates", status_code=200)
async def get_raw_updates(request: Request):
    """Get the raw data for updates"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="updates")
    data = api.raw_data.get("updates", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/level_spec", status_code=200)
async def get_raw_level_spec(request: Request):
    """Get the raw data for level_spec"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="level_spec")
    data = api.raw_data.get("level_spec", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/war_id", status_code=200)
async def get_raw_war_id(request: Request):
    """Get the raw data for war_id"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="war_id")
    data = api.raw_data.get("war_id", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/items", status_code=200)
async def get_raw_items(request: Request):
    """Get the raw data for items"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="items")
    data = api.raw_data.get("items", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/mission_rewards", status_code=200)
async def get_raw_mission_rewards(request: Request):
    """Get the raw data for mission_rewards"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="mission_rewards")
    data = api.raw_data.get("mission_rewards", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/store_rotation", status_code=200)
async def get_raw_store_rotation(request: Request):
    """Get the raw data for store_rotation"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="store_rotation")
    data = api.raw_data.get("store_rotation", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/season_pass", status_code=200)
async def get_raw_season_pass(request: Request):
    """Get the raw data for season_pass"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="season_pass")
    data = api.raw_data.get("season_pass", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/season_pass_hm", status_code=200)
async def get_raw_season_pass_hm(request: Request):
    """Get the raw data for season_pass_hm"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="season_pass_hm")
    data = api.raw_data.get("season_pass_hm", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/season_pass_sv", status_code=200)
async def get_raw_season_pass_sv(request: Request):
    """Get the raw data for season_pass_sv"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="season_pass_sv")
    data = api.raw_data.get("season_pass_sv", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/season_pass_ce", status_code=200)
async def get_raw_season_pass_ce(request: Request):
    """Get the raw data for season_pass_ce"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="season_pass_ce")
    data = api.raw_data.get("season_pass_ce", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/season_pass_dd", status_code=200)
async def get_raw_season_pass_dd(request: Request):
    """Get the raw data for season_pass_dd"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="season_pass_dd")
    data = api.raw_data.get("season_pass_dd", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/season_pass_pp", status_code=200)
async def get_raw_season_pass_pp(request: Request):
    """Get the raw data for season_pass_pp"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="season_pass_pp")
    data = api.raw_data.get("season_pass_pp", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/score_calc", status_code=200)
async def get_raw_score_calc(request: Request):
    """Get the raw data for score_calc"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="score_calc")
    data = api.raw_data.get("score_calc", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/election_candidates", status_code=200)
async def get_raw_election_candidates(request: Request):
    """Get the raw data for election_candidates"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="election_candidates")
    data = api.raw_data.get("election_candidates", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/election_terms", status_code=200)
async def get_raw_election_terms(request: Request):
    """Get the raw data for election_terms"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="election_terms")
    data = api.raw_data.get("election_terms", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/election_policies", status_code=200)
async def get_raw_election_policies(request: Request):
    """Get the raw data for election_policies"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="election_policies")
    data = api.raw_data.get("election_policies", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/minigame_leaderboard", status_code=200)
async def get_raw_minigame_leaderboard(request: Request):
    """Get the raw data for minigame_leaderboard"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="minigame_leaderboard")
    data = api.raw_data.get("minigame_leaderboard", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/player_leaderboard", status_code=200)
async def get_raw_player_leaderboard(request: Request):
    """Get the raw data for player_leaderboard"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="player_leaderboard")
    data = api.raw_data.get("player_leaderboard", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/commend_leaderboard", status_code=200)
async def get_raw_commend_leaderboard(request: Request):
    """Get the raw data for commend_leaderboard"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="commend_leaderboard")
    data = api.raw_data.get("commend_leaderboard", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )


@router.get("/clan_leaderboard", status_code=200)
async def get_raw_clan_leaderboard(request: Request):
    """Get the raw data for clan_leaderboard"""
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="clan_leaderboard")
    data = api.raw_data.get("clan_leaderboard", {}).get("data")
    if data:
        return data
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"204": "No Content"}
    )
