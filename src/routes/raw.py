from fastapi import APIRouter
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
