from pydantic import BaseModel
from typing import Dict, List, Any


class Passive(BaseModel):
    name: str
    description: str


class Armor(BaseModel):
    name: str
    description: str
    type: str
    slot: str
    armor_rating: int
    speed: int
    stamina_regen: int
    passive: Passive | str


class Damage(BaseModel):
    name: str
    description: str
    damage: int


class Weapon(BaseModel):
    name: str
    description: str
    damage: int
    capacity: int
    recoil: int
    fire_rate: int
    fire_mode: List[str]
    traits: List[str]


class Primary(BaseModel):
    type: str


class Grenade(BaseModel):
    name: str
    description: str
    damage: int
    penetration: int
    outer_radius: int
    fuse_time: float


class Weapons(BaseModel):
    primaries: Dict[str, Primary]
    secondaries: Dict[str, Weapon]
    grenades: Dict[str, Grenade]


class Booster(BaseModel):
    name: str
    description: str


class Item(BaseModel):
    name: str
    mix_id: str


class ItemsResponse(BaseModel):
    armor: Dict[str, Armor]
    weapons: Weapons
    boosters: Dict[str, Booster]
    item_list: Dict[str, Item]
