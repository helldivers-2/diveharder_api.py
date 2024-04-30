from fastapi.requests import Request


async def case_sens_middleware(request: Request, call_next):
    decode_format = "utf-8"
    raw_query_str = request.scope["query_string"].decode(decode_format).lower()
    request.scope["query_string"] = raw_query_str.encode(decode_format)

    path = request.scope["path"].lower()
    request.scope["path"] = path

    response = await call_next(request)
    return response
