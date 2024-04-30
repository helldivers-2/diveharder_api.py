from fastapi import APIRouter, HTTPException, status
from fastapi.requests import Request

import src.utils.log as log
from src.cfg.settings import ahgs_api as api_cfg
from src.utils.middleware.authentication import verify_password

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    include_in_schema=True,
    responses={401: {"description": "Unauthorized"}},
)


@router.get("/settings", include_in_schema=False)
async def settings(request: Request, source: str = None):
    if verify_password(request.headers.get("Authorization")):
        log.info(request, status.HTTP_200_OK, source)
        return {
            "log_level": log.logger.level,
            "session_token": api_cfg["auth_headers"].get("Authorization", ""),
        }
    log.info(request, status.HTTP_401_UNAUTHORIZED, source)
    raise HTTPException(status_code=401, detail="Unauthorized")


@router.post("/session", include_in_schema=False)
async def settings(request: Request, source: str = None):
    if verify_password(request.headers.get("Authorization")):
        request_json = await request.json()
        token = request_json["token"]
        if token:
            api_cfg["auth_headers"]["Authorization"] = f"{token}"
            log.info(request, status.HTTP_202_ACCEPTED, source)
            raise HTTPException(status_code=status.HTTP_202_ACCEPTED)
        else:
            log.info(request, status.HTTP_400_BAD_REQUEST, source)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Did not provide token"
            )
    log.info(request, status.HTTP_401_UNAUTHORIZED, source)
    raise HTTPException(status_code=401, detail="Unauthorized")


@router.post("/loglevel", include_in_schema=False)
async def settings(request: Request, source: str = None):
    if verify_password(request.headers.get("Authorization")):
        request_json = await request.json()
        loglevel_in = request_json["loglevel"]
        if loglevel_in:
            log.update_log_level(log_level="loglevel_in")
            log.info(request, status.HTTP_202_ACCEPTED, source)
            raise HTTPException(status_code=status.HTTP_202_ACCEPTED)
        else:
            log.info(request, status.HTTP_400_BAD_REQUEST, source)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Did not provide token"
            )
    log.info(request, status.HTTP_401_UNAUTHORIZED, source)
    raise HTTPException(status_code=401, detail="Unauthorized")
