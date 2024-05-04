from fastapi.requests import Request
from fastapi.responses import PlainTextResponse as PTR
import re


async def rate_limit(request: Request, call_next):
    regex_patterns = [r"Helldivers%20Companion.*", r"Heckdiver.*"]
    client_id = request.headers.get("User-Agent", request.headers.get("X-Super-Client"))

    for pattern in regex_patterns:
        if re.search(pattern, client_id):
            return PTR(status_code=429, content="", headers={"content-type": ""})

    return await call_next(request)
