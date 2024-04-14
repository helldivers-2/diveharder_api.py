from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware


from src.routes import base, admin, raw

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


app.include_router(router)
app.include_router(base.router)
app.include_router(admin.router)
app.include_router(raw.router)
