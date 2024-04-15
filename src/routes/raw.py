from fastapi import APIRouter, status, HTTPException
from fastapi.requests import Request
from src.data.api import handler
import src.utils.log as log

api = handler.api

router = APIRouter()


@router.get("/raw/all", status_code=200)
async def get_all_raw(request: Request, source: str = ""):
    """
    All AHGS API Calls Only\n
    Note: Updates from Steam News are parsed from BBCode to Markdown.\n
    Any AHGS Authenticated API Endpoints may be unreliable at this time.\n
    - We are looking into making them more reliable but until we can generate
      the proper authentication we have to rely on rednecked solutions.\n
    """
    await api.update_all()
    data = {}
    for i, (k, v) in enumerate(api.raw_data.items()):
        if v["data"] is not [] or {}:
            data[k] = v["data"]
    log.info(request, status.HTTP_200_OK, source)
    return data


@router.get("/raw/{data_id}", status_code=200)
async def get_raw(request: Request, data_id: str, source: str = ""):
    """Return api data where id is the key value found in `/raw/all`\n
    Example: `/raw/status` would return the status from `/raw/all`\n
    Note: Updates from Steam News are parsed from BBCode to Markdown."""
    log.info(request, status.HTTP_200_OK, source)
    if data_id in api.raw_data.keys():
        await api.fetch_data(info_name=data_id)
        data = api.raw_data[data_id].get("data")
        return data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
