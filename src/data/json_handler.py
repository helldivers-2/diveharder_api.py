from git import Repo
import os
from json import load, dump

raw_json_data = {}
json_data = {}


def check_if_json_files_exist():
    path = "./src/data/json"
    if os.path.exists(path):
        directory = os.listdir("./src/data/json")
        return len(directory) == 0
    return False


def get_jsons_from_github():
    git_url = "https://github.com/helldivers-2/json"
    path = "./src/data/json"
    Repo.clone_from(git_url, path)


def get_json_files():
    path = "./src/data/json"
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".json"):
                json_path = os.path.join(subdir, file)
                json_base = os.path.basename(json_path)
                json_split = json_base.split(".")[0]
                with open(json_path, "r", encoding="utf-8") as json_file:
                    raw_json_data[json_split] = load(json_file)


def sort_json_dicts():
    global json_data
    json_data = {
        "planets": {
            "planets": raw_json_data["planets"],
            "biomes": raw_json_data["biomes"],
            "environmentals": raw_json_data["environmentals"],
        },
        "items": {
            "armor": {
                "list": raw_json_data["armor"],
                "passives": raw_json_data["passive"],
                "slots": raw_json_data["slot"],
            },
            "weapons": {
                "primaries": raw_json_data["primary"],
                "secondaries": raw_json_data["secondary"],
                "grenades": raw_json_data["grenades"],
                "fire_modes": raw_json_data["fire_modes"],
                "traits": raw_json_data["traits"],
                "types": raw_json_data["types"],
            },
            "boosters": raw_json_data["boosters"],
            "item_list": raw_json_data["item_names"],
        },
        "warbonds": {
            "helldivers_mobilize": raw_json_data["helldivers_mobilize"],
            "steeled_veterans": raw_json_data["steeled_veterans"],
            "cutting_edge": raw_json_data["cutting_edge"],
            "democratic_detonation": raw_json_data["democratic_detonation"],
        },
        "factions": raw_json_data["factions"],
    }


def expand_json():
    # Handle Planets
    global json_data
    for i, (k, v) in enumerate(json_data["planets"]["planets"].items()):
        # Handle Planet Biomes
        v["biome"] = raw_json_data["biomes"][v["biome"]]
        # Handle Planet Environmentals
        environ_array = []
        for envrion in v["environmentals"]:
            environ_array.append(raw_json_data["environmentals"].get(envrion, ""))
        v["environmentals"] = environ_array
    json_data["planets"] = json_data["planets"]["planets"]

    # Handle Items
    # Handle Armors
    for i, (k, v) in enumerate(json_data["items"]["armor"]["list"].items()):
        match v["type"]:
            case 0:
                v["type"] = "Light"
            case 1:
                v["type"] = "Medium"
            case 2:
                v["type"] = "Heavy"
        v["slot"] = json_data["items"]["armor"]["slots"][str(v["slot"])]
        v["passive"] = json_data["items"]["armor"]["passives"].get(
            str(v["passive"]), "ERROR"
        )
    json_data["items"]["armor"] = json_data["items"]["armor"]["list"]

    # Handle Primary Weapons
    for i, (k, v) in enumerate(json_data["items"]["weapons"]["primaries"].items()):
        v["type"] = json_data["items"]["weapons"]["types"][str(v["type"])]
        modes = []
        for mode in v["fire_mode"]:
            modes.append(json_data["items"]["weapons"]["fire_modes"][str(mode)])
        v["fire_mode"] = modes
        traits = []
        for trait in v["traits"]:
            traits.append(json_data["items"]["weapons"]["traits"][str(trait)])
        v["traits"] = traits

    # Handle Primary Weapons
    for i, (k, v) in enumerate(json_data["items"]["weapons"]["secondaries"].items()):
        modes = []
        for mode in v["fire_mode"]:
            print(v["name"], "Mode: ", mode)
            modes.append(json_data["items"]["weapons"]["fire_modes"][str(mode)])
        v["fire_mode"] = modes
        traits = []
        for trait in v["traits"]:
            traits.append(json_data["items"]["weapons"]["traits"][str(trait)])
        v["traits"] = traits

    json_data["items"]["weapons"].pop("fire_modes")
    json_data["items"]["weapons"].pop("traits")
    json_data["items"]["weapons"].pop("types")

    # Handle Warbonds
    for i, (warbond_key, warbond) in enumerate(json_data["warbonds"].items()):
        # enumerate through each warbond page
        for j, (page_key, page) in enumerate(warbond.items()):
            # Create Holding Array
            page["assets"] = {}
            # iterate through each item of the page
            for item in page["items"]:
                item_id = str(item["item_id"])
                page["assets"][item_id] = json_data["items"]["item_list"].get(
                    item_id, {"error": "404"}
                )
                if item_id in json_data["items"]["armor"].keys():
                    page["assets"][item_id].update(json_data["items"]["armor"][item_id])
                if item_id in json_data["items"]["weapons"]["primaries"].keys():
                    page["assets"][item_id].update(
                        json_data["items"]["weapons"]["primaries"][item_id]
                    )
                elif item_id in json_data["items"]["weapons"]["secondaries"].keys():
                    page["assets"][item_id].update(
                        json_data["items"]["weapons"]["secondaries"][item_id]
                    )
                elif item_id in json_data["items"]["weapons"]["grenades"].keys():
                    page["assets"][item_id].update(
                        json_data["items"]["weapons"]["grenades"][item_id]
                    )
                page["assets"][item_id].update({"medal_cost": item["medal_cost"]})
            page["items"] = page["assets"]
            page.pop("assets")


get_json_files()
sort_json_dicts()
expand_json()

with open("./testing.json", "w", encoding="utf-8") as f:
    dump(json_data, f, ensure_ascii=False, indent=4)
