from fastapi import FastAPI
from src.utils.api_singleton import fast_app as fast_app
from src.routes import base, admin, raw, v1

app: FastAPI = fast_app

app.include_router(base.router)
app.include_router(admin.router)
app.include_router(raw.router)
app.include_router(v1.router)
