from fastapi import APIRouter, status
from src.data.api import handler

api = handler.api

router = APIRouter()


@router.get("/raw/all", status_code=200)
async def get_all_raw(source: str = ""):
    """
    All AHGS API Calls Only
    """
    update = await api.update_all()
    data = {}
    for i, (k, v) in enumerate(api.raw_data.items()):
        if v["data"] is not [] or {}:
            data[k] = v["data"]
    return data


@router.get("/raw/{id}", status_code=200)
async def get_raw(id: str):
    """Return api data where id is the key value found in `/raw/all`\n
    Example: `/raw/status` would return the status from `/raw/all`"""
    update = await api.update_all()
    info = api.raw_data.get(id, {"error": status.HTTP_400_BAD_REQUEST})
    data = info.get("data")
    return data
