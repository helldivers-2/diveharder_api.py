from fastapi import APIRouter, status, HTTPException
from fastapi.requests import Request
from starlette.responses import RedirectResponse

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
    All AHGS API Calls Only\n
    Note: Updates from Steam News are parsed from BBCode to Markdown.\n
    Any AHGS Authenticated API Endpoints may be unreliable at this time.\n
    - We are looking into making them more reliable but until we can generate
      the proper authentication we have to rely on rednecked solutions.\n
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
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="status")
    data = api.raw_data["status"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/war_info", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="war_info")
    data = api.raw_data["war_info"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/planetstats", include_in_schema=False)
@router.get("/planet_stats")
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="planet_stats")
    data = api.raw_data["planet_stats"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/major_order", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="major_order")
    data = api.raw_data["major_order"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/news_feed", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="news_feed")
    data = api.raw_data["news_feed"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/updates", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="updates")
    data = api.raw_data["updates"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/war_id", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="war_id")
    data = api.raw_data["war_id"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/items", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="war_id")
    data = api.raw_data["war_id"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/minigame_leaderboard", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="minigame_leaderboard")
    data = api.raw_data["minigame_leaderboard"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/player_leaderboard", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="player_leaderboard")
    data = api.raw_data["player_leaderboard"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/commend_leaderboard", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="commend_leaderboard")
    data = api.raw_data["commend_leaderboard"].get("data")
    if data:
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/clan_leaderboard", status_code=200)
async def redirect_planetstats(request: Request):
    log.info(request, status.HTTP_200_OK)
    await api.fetch_data(info_name="clan_leaderboard")
    data = api.raw_data["clan_leaderboard"].get("data")
    if not data:
        return {}
    return data
