import bcrypt

from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.cfg.settings import security

TOKEN = security["token"]
hashed = bcrypt.hashpw(bytes(TOKEN, "utf-8"), bcrypt.gensalt())


async def authenticate(request: Request, call_next):
    authenticated_prefixes = "admin"
    response = None
    headers = dict(request.scope["headers"])
    if (
        authenticated_prefixes in request.url.path
        and "authorization" in request.headers
    ):
        if verify_password(request.headers["Authorization"]):
            response = await call_next(request)
        else:
            response = JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"error": "Unauthorized"},
            )
    else:
        response = await call_next(request)
    return response


def verify_length(token):
    length = len(token)
    if length <= 7 or length >= 25:
        return False
    return True


def verify_password(plaintext_token):
    if verify_length(plaintext_token):
        if bcrypt.checkpw(str.encode(plaintext_token), hashed):
            return True
        else:
            return False
