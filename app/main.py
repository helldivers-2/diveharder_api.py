from contextlib import asynccontextmanager
from time import gmtime, strftime
import os
from fastapi import APIRouter, FastAPI
from fastapi.requests import Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import app.data.api as apiv1
import asyncio
from app.models.arrowhead.warStatus import WarStatus

description = """
Python FastAPI proxy server for the Helldivers 2 API.
"""


async def update_data(isForce: bool = True, interval: int = 20):
    while True:
        await api_v1.update(force=isForce)
        await asyncio.sleep(interval)


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(update_data())
    yield


HD2API = FastAPI(
    title="Helldivers 2 Community API",
    openapi_url="/openapi.json",
    description=description,
    lifespan=lifespan,
)


api_v1 = apiv1.API()
DECODE_FORMAT = "latin-1"


router = APIRouter()


@router.get("/", status_code=200)
def root():
    """Root Get"""
    return {
        "greeting": "Liberty's Greetings, Helldiver!",
        "docs": "https://api.diveharder.com/docs",
        "redocs": "https://api.diveharder.com/redoc",
        "git": "aHR0cHM6Ly9naXRsYWIuY29tL2NoYXR0ZXJjaGF0cy9oZDItY29tbXVuaXR5LWFwaS8",
        "discord": "MTU1MTQ4NjY2MjU5MTExOTM2",
        "apiTime": strftime("%Y-%m-%d %H:%M:%S", gmtime(api_v1.update_time)),
    }


@router.get("/all", status_code=200)
def get_all():
    """
    All AHGS API plus Races, Planet Names, and Sectors
    """

    return api_v1.all_responses


@router.get("/races", status_code=200)
def get_races():
    return api_v1.races


@router.get("/planetnames", status_code=200)
def get_planet_names():
    return api_v1.planet_names


@router.get("/sectors", status_code=200)
def get_sectors():
    return api_v1.sectors


@router.get("/raw/status", status_code=200)
def get_raw_status() -> WarStatus:
    return api_v1.status_response


@router.get("/raw/warinfo", status_code=200)
def get_raw_warinfo():
    return api_v1.warinfo_response


@router.get("/raw/planetstats", status_code=200)
def get_raw_planetstats():
    return api_v1.planet_stats_response


@router.get("/raw/newsticker", status_code=200)
def get_raw_newsticker():
    return api_v1.news_ticker_response


@router.get("/raw/newsfeed", status_code=200)
def get_raw_newsfeed():
    return api_v1.news_feed_response


@router.get("/raw/timesincestart", status_code=200)
def get_raw_timesincestart():
    return api_v1.timesincestart_response


@router.get("/raw/warid", status_code=200)
def get_raw_warid():
    return api_v1.warid_response


@router.get("/raw/galacticwareffects", status_code=200)
def get_raw_galacticwareffects():
    return api_v1.galactic_war_effects_response


@router.get("/raw/levelspec", status_code=200)
def get_raw_levelspec():
    return api_v1.levelspec_response


@router.get("/raw/items", status_code=200)
def get_raw_items():
    return api_v1.items_api_response


@router.get("/raw/missionrewards", status_code=200)
def get_raw_missionrewards():
    return api_v1.mission_reward_response


@router.get("/raw/majororder", status_code=200)
def get_raw_majororder():
    return api_v1.major_order_response


@router.get("/raw/all", status_code=200)
def get_all_raw():
    """
    All AHGS API Calls Only
    """

    return api_v1.all_raw_responses


@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    base_path = os.path.dirname(__file__)
    favicon = os.path.join(base_path, "favicon.ico")
    return FileResponse(favicon)


HD2API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@HD2API.middleware("http")
async def case_sens_middleware(request: Request, call_next):
    raw_query_str = request.scope["query_string"].decode(DECODE_FORMAT).lower()
    request.scope["query_string"] = raw_query_str.encode(DECODE_FORMAT)

    path = request.scope["path"].lower()
    request.scope["path"] = path

    response = await call_next(request)
    return response


HD2API.include_router(router)
