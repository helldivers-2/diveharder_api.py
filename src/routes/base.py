from fastapi import APIRouter, status
from fastapi.requests import Request
from fastapi.responses import FileResponse

import src.utils.log as log

router = APIRouter(include_in_schema=False)


@router.get("/")
async def root(request: Request, source: str = None):
    # Base level route. Useful for health checks.
    log.info(request, status.HTTP_200_OK, source)
    return {
        "msg": "You made it, Helldiver! Sit, and have a drink!",
        "raw_data": "https://api.diveharder.com/raw/all",
        "formatted_data": "https://api.diveharder.com/v1/all",
    }


@router.get("/favicon.ico")
async def favicon():
    # Provides an icon for those who visit the site.
    return FileResponse("src/favicon.ico", media_type="image/x-icon")
