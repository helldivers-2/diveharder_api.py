from fastapi import APIRouter, status
from fastapi.requests import Request
from fastapi.responses import FileResponse

import src.utils.log as log

router = APIRouter()


@router.get("/")
async def root(request: Request, source: str = None):
    # Base level route. Useful for health checks.
    log.info(request, status.HTTP_200_OK, source)
    return "Good Job"


@router.get("/favicon.ico")
async def favicon():
    # Provides an icon for those who visit the site.
    return FileResponse("src/favicon.ico", media_type="image/x-icon")
