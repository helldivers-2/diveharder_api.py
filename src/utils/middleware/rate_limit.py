import src.utils.log as log
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import re


async def cutoff(request: Request, call_next):
    regex_pattern = r"Helldivers%20Companion.*CFNetwork.*Darwin"

    decode_format = "utf-8"
    raw_query_str = request.headers.get("User-Agent", "")
    if re.search(regex_pattern, raw_query_str):
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
