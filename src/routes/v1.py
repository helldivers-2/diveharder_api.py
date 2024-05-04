from fastapi import APIRouter, status
from fastapi.requests import Request
from time import strftime, localtime

from src.data.api import handler
import src.utils.log as log
from src.data.json_handler import json_data, helper_data

router = APIRouter(prefix="/v1", tags=["v1"], include_in_schema=True)

api = handler.api

no_include = [
    "mission_rewards",
    "level_spec",
    "score_calc",
    "season_pass",
    "season_pass_hm",
    "season_pass_sv",
    "season_pass_ce",
    "season_pass_dd",
]


async def update_data():
    data = {
        k: v["data"]
        for k, v in api.raw_data.items()
        if v["data"] and k not in no_include
    }
    data.update(json_data)
    data["store_rotation"] = await update_store_data(data.get("store_rotation", {}))
    data["player_leaderboard"] = data.get("player_leaderboard", {}).get("entries", [])
    data["commend_leaderboard"] = data.get("commend_leaderboard", {}).get("entries", [])
    return data


def get_buy_price_amount(item_id=None, mix_id=None):
    item = next(
        (
            item
            for item in api.raw_data.get("items", []).get("data", {})
            if (item_id is not None and str(item.get("itemId")) == item_id)
            or (
                mix_id is not None
                and str(item.get("mix_id")) is not None
                and str(mix_id) == mix_id
            )
        ),
        None,
    )
    if "buyPrice" in item and len(item["buyPrice"]) > 0:
        return item["buyPrice"][0]["amount"]  # Assuming only one buy price
    else:
        return None  # No buy price available


async def update_store_data(data):
    expire_time = strftime("%d-%b-%Y %H:%M", localtime(int(data["expireTime"])))

    store_items = [
        str(item["mixId"]) for item in data["salesPage"]["sections"][0]["items"]
    ]
    for k, v in helper_data["item_list"].items():
        if v["mix_id"] in store_items:
            index = store_items.index(v["mix_id"])
            store_items[index] = k
        elif k in store_items:
            index = store_items.index(k)
            store_items[index] = k
    items = []
    for item in store_items:
        if item in json_data["items"]["armor"]:
            item_data = json_data["items"]["armor"][item]
            item_data.update({"store_cost": get_buy_price_amount(item)})
            items.append(item_data)
        else:
            items.append({"name": "Unmapped"})
    return {"expire_time": expire_time, "items": items}


@router.get("/all")
async def get_all(request: Request):
    """
    All AHGS API Calls + Formatted Versions provided by me\n
    Note: Updates from Steam News are parsed from BBCode to Markdown.\n
    Any AHGS Authenticated API Endpoints may be unreliable at this time.\n
    - We are looking into making them more reliable but until we can generate
      the proper authentication we have to rely on rednecked solutions.\n
    """
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    return data


@router.get("/{data_id}")
async def get_data(request: Request, data_id):
    log.info(request, status.HTTP_200_OK)
    await api.update_all()
    data = await update_data()
    return data[data_id]
