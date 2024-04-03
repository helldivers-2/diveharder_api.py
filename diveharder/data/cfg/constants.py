import json

api = {
    "REQUEST_HEADERS": {
        "Accept-Language": "en-US",
        "User-Agent": "Helldivers 2 Community API",
    },
}

planets = {
    "names": json.load(open("./json/planets.json")),
    "sectors": json.load(open("./json/sectors.json")),
}

faction = {
    "names": json.load(open("./json/factions.json")),
}
