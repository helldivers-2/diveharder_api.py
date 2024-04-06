import json
import os
import requests
from .settings import session_token

api = {
    "REQUEST_HEADERS": {
        "Accept-Language": "en-US",
        "User-Agent": "Helldivers 2 Community API",
    },
    "AUTH_REQUEST_HEADERS": {
        "Accept-Language": "en-US",
        "User-Agent": "Helldivers 2 Community API",
        "Authorization": session_token,
    },
}

files = ["planets.json", "sectors.json", "factions.json"]
path = "./json/"
repo_url = os.environ.get("FILES_URL")

def load_json(file: str):
    file_url = repo_url + file
    response = requests.get(file_url, timeout=5)
    response.raise_for_status()

    os.makedirs(path, exist_ok=True)

    with open(path + file, "w") as f:
        f.write(response.text)


check_files = [load_json(file) for file in files if not os.path.exists(path + file)]

planets = {
    "names": json.load(open("./json/planets.json")),
    "sectors": json.load(open("./json/sectors.json")),
}

faction = {
    "names": json.load(open("./json/factions.json")),
}
