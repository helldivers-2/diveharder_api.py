from fastapi.testclient import TestClient
import time
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from app.main import HD2API  # noqa: E402


TIMEOUT = 15
test_units = {
    "BASE": "/",
    "DOCS": "/docs",
    "RACES": "/races",
    "PLANET_NAMES": "/planetnames",
    "SECTORS": "/sectors",
    "RAW_STATUS": "/raw/status",
    "RAW_WARINFO": "/raw/warinfo",
    "RAW_PLANET_STATS": "/raw/planetstats",
    "RAW_NEWS_TICKER": "/raw/newsticker",
    "RAW_NEWS_FEED": "/raw/newsfeed",
    "RAW_TIME_SINCE_START": "/raw/timesincestart",
    "RAW_WARID": "/raw/warid",
    "RAW_GALACTICWAREFFECTS": "/raw/galacticwareffects",
    "RAW_LEVELSPEC": "/raw/levelspec",
    "RAW_ITEMS": "/raw/items",
    "RAW_MISSION_REWARDS": "/raw/missionrewards",
    "RAW_MAJOR_ORDER": "/raw/majororder",
    "RAW_ALL": "/raw/all",
}

client = TestClient(HD2API)


def test_get():
    count = 0
    for value in test_units.values():
        time.sleep(1)
        response = client.get(value)
        status = response.status_code
        if status == 200:
            count += 1
    full_count = len(test_units)
    grade = count / full_count
    assert grade >= 0.95


def test_cache():
    print("Running test GET again for Cache Testing")
    time.sleep(20)
    test_get()


if __name__ == "__main__":
    test_get()
