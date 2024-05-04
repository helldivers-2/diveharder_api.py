from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

# Middleware Improts
from starlette.middleware.cors import CORSMiddleware
from brotli_asgi import BrotliMiddleware
from src.utils.middleware.case_sens_middleware import case_sens_middleware
from src.utils.middleware.rate_limit import rate_limit
from src.utils.middleware.metrics import instrumentator
from src.utils.middleware.authentication import authenticate

# Routes Import
from src.routes import base, admin, raw, v1, webhook_in

# -------- INIT API -------- #
app: FastAPI = FastAPI(
    title="HD2 Community API",
    openapi_url="/openapi.json",
    description="""
    Proxy API for Helldivers 2, providing access to backend game systems
    used by Helldivers 2. Built on the Python FastAPI framework.
    Discord: chatterchats
    Github: https://github.com/helldivers-2/diveharder_api.py/""",
)

# -------- MIDDLEWARE -------- #
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(BrotliMiddleware, minimum_size=500)
app.add_middleware(BaseHTTPMiddleware, dispatch=case_sens_middleware)
app.add_middleware(BaseHTTPMiddleware, dispatch=authenticate)
instrumentator.instrument(app=app).expose(
    app, include_in_schema=False, should_gzip=True
)
app.add_middleware(BaseHTTPMiddleware, dispatch=rate_limit)
# -------- ROUTES -------- #
app.include_router(base.router)
app.include_router(admin.router)
app.include_router(raw.router)
app.include_router(v1.router)

# -------- WEBHOOK -------- #
app.include_router(webhook_in.router)
