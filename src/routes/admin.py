from fastapi import APIRouter, HTTPException, status
from fastapi.requests import Request

import src.utils.log as log
from src.cfg.settings import ahgs_api as api_cfg

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    include_in_schema=False,
)


@router.get("/settings")
async def settings(request: Request):
    log.info(request, status.HTTP_200_OK)
    return {
        "log_level": log.logger.level,
        "session_token": api_cfg["auth_headers"].get("Authorization", ""),
    }


@router.post("/session")
async def settings(request: Request):
    request_json = await request.json()
    token = request_json["token"]
    if token:
        api_cfg["auth_headers"]["Authorization"] = f"{token}"
        log.info(request, status.HTTP_202_ACCEPTED)
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED)
    else:
        log.info(request, status.HTTP_400_BAD_REQUEST)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Did not provide token"
        )


@router.post("/loglevel")
async def settings(request: Request):
    request_json = await request.json()
    loglevel_in = request_json["loglevel"]
    if loglevel_in:
        log.update_log_level(log_level="loglevel_in")
        log.info(request, status.HTTP_202_ACCEPTED)
        raise HTTPException(status_code=status.HTTP_202_ACCEPTED)
    else:
        log.info(request, status.HTTP_400_BAD_REQUEST)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Did not provide token"
        )
