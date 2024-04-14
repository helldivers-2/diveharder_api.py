from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from src.data import api
from src.routes import base, admin

api = api.API()

app = FastAPI(
    title="HD2 Community API",
    openapi_url="/openapi.json",
    description="""
    Proxy API for Helldivers 2, providing access to backend game systems
    used by Helldivers 2. Built on the Python FastAPI framework.
    Contact: chatterchats@discord""",
)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


app.include_router(router)
app.include_router(base.router)
app.include_router(admin.router)
