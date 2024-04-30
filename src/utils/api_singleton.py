from fastapi import FastAPI


fast_app = FastAPI(
    title="HD2 Community API",
    openapi_url="/openapi.json",
    description="""
    Proxy API for Helldivers 2, providing access to backend game systems
    used by Helldivers 2. Built on the Python FastAPI framework.
    Discord: chatterchats
    Github: https://github.com/helldivers-2/diveharder_api.py/""",
)
