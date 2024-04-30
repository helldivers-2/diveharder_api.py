from src.utils.api_singleton import fast_app as fast_app

from starlette.middleware.cors import CORSMiddleware
from brotli_asgi import BrotliMiddleware

fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
fast_app.add_middleware(BrotliMiddleware)
