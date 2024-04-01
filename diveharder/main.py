# STD LIB IMPORTS
from contextlib import asynccontextmanager
from time import gmtime, strftime, sleep
from typing import List
import os

# FASTAPI IMPORTS
from fastapi import APIRouter, FastAPI, status, HTTPException
from fastapi.requests import Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# API CLASS IMPORT
import diveharder.data.api as api

# DATA MODEL IMPORTS
from diveharder.models.arrowhead.imports import *
from diveharder.models.steam.news import NewsItem

# LOGGER IMPORT
from diveharder.utils.logging import logger, log, update_log_level

description = """
Python FastAPI proxy server for the Helldivers 2 API.
"""


async def update_data(isForce: bool = False):
    await api_handler.update(force=isForce)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await update_data(isForce=True)
    yield


API = FastAPI(
    title="Helldivers 2 Community API",
    openapi_url="/openapi.json",
    description=description,
    lifespan=lifespan,
)


api_handler = api.API()


router = APIRouter()


@router.get("/", status_code=200)
async def root(request: Request):
    """Root Get"""
    log(request, status.HTTP_200_OK)
    return {
        "greeting": "Liberty's Greetings, Helldiver!",
        "docs": "https://api.diveharder.com/docs",
        "redocs": "https://api.diveharder.com/redoc",
        "git": "aHR0cHM6Ly9naXRsYWIuY29tL2NoYXR0ZXJjaGF0cy9oZDItY29tbXVuaXR5LWFwaS8",
        "discord": "MTU1MTQ4NjY2MjU5MTExOTM2",
        "apiTime": strftime("%Y-%m-%d %H:%M:%S", gmtime(api_handler.update_time)),
    }


@router.get("/admin/", include_in_schema=False, status_code=200)
async def return_logger():
    return {"logLevel": logger.level}


@router.get("/admin/{loggingLevel}", include_in_schema=False, status_code=200)
async def update_logger(loggingLevel: int) -> None:
    update_log_level(logLevel=loggingLevel)
    logger.debug("DEBUG TEST AFTER UPDATE")
    logger.info("INFO TEST AFTER UPDATE")
    return None


@router.get("/all", status_code=200)
async def get_all(request: Request):
    """
    All AHGS API plus Races, Planet Names, and Sectors
    """
    await update_data(isForce=False)
    data = api_handler.all_responses
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/races", status_code=200)
async def get_races(request: Request):
    data = api_handler.races
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/planetnames", status_code=200)
async def get_planet_names(request: Request):
    data = api_handler.planet_names
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/sectors", status_code=200)
async def get_sectors(request: Request):
    data = api_handler.sectors
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/status", status_code=200)
async def get_raw_status(request: Request) -> WarStatus:
    await update_data(isForce=False)
    data = api_handler.status_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/warinfo", status_code=200)
async def get_raw_warinfo(request: Request) -> WarInfo:
    await update_data(isForce=False)
    data = api_handler.warinfo_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/planetstats", status_code=200)
async def get_raw_planetstats(request: Request) -> WarSummary:
    await update_data(isForce=False)
    data = api_handler.planet_stats_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/newsticker", status_code=200)
async def get_raw_newsticker(request: Request) -> NewsTicker:
    data = api_handler.news_ticker_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/newsfeed", status_code=200)
async def get_raw_newsfeed(request: Request) -> List[NewsFeedItem]:
    data = api_handler.news_feed_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/timesincestart", status_code=200)
async def get_raw_timesincestart(request: Request) -> TimeSinceStart:
    await update_data(isForce=False)
    data = api_handler.timesincestart_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/warid", status_code=200)
async def get_raw_warid(request: Request) -> WarID:
    data = api_handler.warid_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/galacticwareffects", status_code=200)
async def get_raw_galacticwareffects(request: Request) -> List[GalacticWarEffect]:
    data = api_handler.galactic_war_effects_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/levelspec", status_code=200)
async def get_raw_levelspec(request: Request) -> List[Level]:
    data = api_handler.levelspec_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/leaderboard", status_code=200)
async def get_raw_leaderboard(request: Request) -> Leaderboard | Error:
    """
    This may or may not break... There's a lot of bugs with this on AHGS' side.
    """
    data = api_handler.leaderboard_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/items", status_code=200)
async def get_raw_items(request: Request) -> List[Item]:
    data = api_handler.items_api_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/missionrewards", status_code=200)
async def get_raw_missionrewards(request: Request) -> MissionRewards:
    data = api_handler.mission_reward_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/majororder", status_code=200)
async def get_raw_majororder(request: Request) -> List[Assignment]:
    await update_data(isForce=False)
    data = api_handler.major_order_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/updates", status_code=200)
async def get_steam_news(request: Request) -> List[NewsItem]:
    await update_data(isForce=False)
    data = api_handler.steam_news_response
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/raw/all", status_code=200)
async def get_all_raw(request: Request) -> AllRaw:
    """
    All AHGS API Calls Only
    """
    await update_data(isForce=False)
    data = api_handler.all_raw_responses
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


@router.get("/favicon.ico", include_in_schema=False)
async def favicon(request: Request):
    base_path = os.path.dirname(__file__)
    data = os.path.join(base_path, "favicon.ico")
    if data:
        log(request, status.HTTP_200_OK)
        return data
    else:
        log(request, status.HTTP_204_NO_CONTENT)
        return HTTPException(status.HTTP_204_NO_CONTENT)


API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.middleware("http")
async def case_sens_middleware(request: Request, call_next):
    DECODE_FORMAT = "latin-1"
    raw_query_str = request.scope["query_string"].decode(DECODE_FORMAT).lower()
    request.scope["query_string"] = raw_query_str.encode(DECODE_FORMAT)

    path = request.scope["path"].lower()
    request.scope["path"] = path

    response = await call_next(request)
    return response


API.include_router(router)
