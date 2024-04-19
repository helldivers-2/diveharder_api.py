from fastapi import APIRouter, status
from fastapi.requests import Request
from time import strftime, localtime

from src.data.api import handler
import src.utils.log as log
from src.data.json_handler import json_data, helper_data

router = APIRouter(prefix="/v1", tags=["v1"], include_in_schema=True)

api = handler.api


async def update_data():
    data_pop_list = [
        "season_pass",
        "season_pass_hm",
        "season_pass_sv",
        "season_pass_ce",
        "season_pass_dd",
    ]
    data = {}
    for i, (k, v) in enumerate(api.raw_data.items()):
        if v["data"] is not [] or {}:
            data[k] = v["data"]
    for popper in data_pop_list:
        if popper in data:
            data.pop(popper)
    data.update(json_data)
    if data["store_rotation"]:
        data["store_rotation"] = await update_store_data(data["store_rotation"])
    return data


async def update_store_data(data):
    store_items = [item["mixId"] for item in data["salesPage"]["sections"][0]["items"]]
    for i, (k, v) in enumerate(helper_data["item_list"].items()):
        if int(v["mix_id"]) in store_items:
            index = store_items.index(int(v["mix_id"]))
            store_items[index] = k
        elif int(k) in store_items:
            index = store_items.index(int(k))
            store_items[index] = k
    expire_time = strftime("%d-%b-%Y %H:%M", localtime(int(data["expireTime"])))
    items = []
    for item in store_items:
        if item in json_data["items"]["armor"]:
            items.append(json_data["items"]["armor"][item])
        else:
            items.append({"name": "Unmapped"})
    return {"expire_time": expire_time, "items": items}


@router.get("/all")
async def get_all(request: Request, source: str = ""):
    global formatted_data
    """
    All AHGS API Calls + Formatted Versions provided by me\n
    Note: Updates from Steam News are parsed from BBCode to Markdown.\n
    Any AHGS Authenticated API Endpoints may be unreliable at this time.\n
    - We are looking into making them more reliable but until we can generate
      the proper authentication we have to rely on rednecked solutions.\n
    """
    log.info(request, status.HTTP_200_OK, source)
    await api.update_all()
    data = await update_data()
    return data


@router.get("/{data_id}")
async def get_data(request: Request, data_id, source: str = ""):
    log.info(request, status.HTTP_200_OK, source)
    await api.update_all()
    data = await update_data()
    return data[data_id]
