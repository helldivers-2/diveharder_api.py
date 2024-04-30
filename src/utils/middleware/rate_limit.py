from src.utils.api_singleton import fast_app as fast_app
import src.utils.log as log
from fastapi.requests import Request
from fastapi.responses import JSONResponse


@fast_app.middleware("http")
async def cutoff(request: Request, call_next):
    block_list = "Helldivers%20Companion/238 CFNetwork/1494.0.7 Darwin/23.4.0"
    decode_format = "utf-8"
    raw_query_str = request.headers.get("User-Agent", "")
    if block_list == raw_query_str:
        log.info(request, 429, block_list)
        response = JSONResponse(
            status_code=429,
            content={
                "limited": "Contact @chatterchats on Discord.",
            },
        )
        return response
    else:
        response = await call_next(request)
        return response
