from fastapi import FastAPI, APIRouter
from fastapi.requests import Request
from starlette.middleware.cors import CORSMiddleware


from src.routes import base, admin, raw

app = FastAPI(
    title="HD2 Community API",
    openapi_url="/openapi.json",
    description="""
    Proxy API for Helldivers 2, providing access to backend game systems
    used by Helldivers 2. Built on the Python FastAPI framework.
    Discord: chatterchats
    Github: https://github.com/helldivers-2/diveharder_api.py/""",
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


@app.middleware("http")
async def case_sens_middleware(request: Request, call_next):
    decode_format = "utf-8"
    raw_query_str = request.scope["query_string"].decode(decode_format).lower()
    request.scope["query_string"] = raw_query_str.encode(decode_format)

    path = request.scope["path"].lower()
    request.scope["path"] = path

    response = await call_next(request)
    return response


app.include_router(router)
app.include_router(base.router)
app.include_router(admin.router)
app.include_router(raw.router)
