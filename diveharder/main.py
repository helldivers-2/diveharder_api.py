# STD LIB IMPORTS
from contextlib import asynccontextmanager
from time import gmtime, strftime, sleep
from typing import List
import os

# FASTAPI IMPORTS
from fastapi import APIRouter, FastAPI
from fastapi.requests import Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# API CLASS IMPORT
import diveharder.data.api as api

# DATA MODEL IMPORTS
from diveharder.models.arrowhead.imports import *

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
async def root():
    """Root Get"""
    return {
        "greeting": "Liberty's Greetings, Helldiver!",
        "docs": "https://api.diveharder.com/docs",
        "redocs": "https://api.diveharder.com/redoc",
        "git": "aHR0cHM6Ly9naXRsYWIuY29tL2NoYXR0ZXJjaGF0cy9oZDItY29tbXVuaXR5LWFwaS8",
        "discord": "MTU1MTQ4NjY2MjU5MTExOTM2",
        "apiTime": strftime("%Y-%m-%d %H:%M:%S", gmtime(api_handler.update_time)),
    }


@router.get("/all", status_code=200)
async def get_all():
    """
    All AHGS API plus Races, Planet Names, and Sectors
    """
    await update_data(isForce=False)
    return api_handler.all_responses


@router.get("/races", status_code=200)
async def get_races():
    return api_handler.races


@router.get("/planetnames", status_code=200)
async def get_planet_names():
    return api_handler.planet_names


@router.get("/sectors", status_code=200)
async def get_sectors():
    return api_handler.sectors


@router.get("/raw/status", status_code=200)
async def get_raw_status() -> WarStatus:
    await update_data(isForce=False)
    return api_handler.status_response


@router.get("/raw/warinfo", status_code=200)
async def get_raw_warinfo() -> WarInfo:
    await update_data(isForce=False)
    return api_handler.warinfo_response


@router.get("/raw/planetstats", status_code=200)
async def get_raw_planetstats() -> WarSummary:
    await update_data(isForce=False)
    return api_handler.planet_stats_response


@router.get("/raw/newsticker", status_code=200)
async def get_raw_newsticker() -> NewsTicker:
    return api_handler.news_ticker_response


@router.get("/raw/newsfeed", status_code=200)
async def get_raw_newsfeed() -> List[NewsFeedItem]:
    return api_handler.news_feed_response


@router.get("/raw/timesincestart", status_code=200)
async def get_raw_timesincestart() -> TimeSinceStart:
    await update_data(isForce=False)
    return api_handler.timesincestart_response


@router.get("/raw/warid", status_code=200)
async def get_raw_warid() -> WarID:
    return api_handler.warid_response


@router.get("/raw/galacticwareffects", status_code=200)
async def get_raw_galacticwareffects() -> List[GalacticWarEffect]:
    return api_handler.galactic_war_effects_response


@router.get("/raw/levelspec", status_code=200)
async def get_raw_levelspec() -> List[Level]:
    return api_handler.levelspec_response


@router.get("/raw/leaderboard", status_code=200)
async def get_raw_leaderboard() -> Leaderboard | Error:
    """
    This may or may not break... There's a lot of bugs with this on AHGS' side.
    """
    return api_handler.leaderboard_response


@router.get("/raw/items", status_code=200)
async def get_raw_items() -> List[Item]:
    return api_handler.items_api_response


@router.get("/raw/missionrewards", status_code=200)
async def get_raw_missionrewards() -> MissionRewards:
    return api_handler.mission_reward_response


@router.get("/raw/majororder", status_code=200)
async def get_raw_majororder() -> List[Assignment]:
    await update_data(isForce=False)
    return api_handler.major_order_response


@router.get("/raw/updates", status_code=200)
async def get_steam_news():
    await update_data(isForce=False)
    return api_handler.steam_news_response


@router.get("/raw/all", status_code=200)
async def get_all_raw() -> AllRaw:
    """
    All AHGS API Calls Only
    """
    await update_data(isForce=False)
    return api_handler.all_raw_responses


@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    base_path = os.path.dirname(__file__)
    favicon = os.path.join(base_path, "favicon.ico")
    return FileResponse(favicon)


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
