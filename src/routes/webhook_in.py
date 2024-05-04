from fastapi import APIRouter, status, HTTPException
from fastapi.requests import Request
from starlette.responses import Response
import json
from src.data.json_handler import update_json
import src.utils.log as log
from src.cfg.settings import security
import hashlib
import hmac

router = APIRouter(
    prefix="/wh",
    tags=["webhook"],
    include_in_schema=False,
)


class Webhook:
    def __init__(self, token):
        self.token = token

    def github_verify(self, payload, headers):
        signature_header = headers.get("x-hub-signature-256", None)
        if not signature_header:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="x-hub-signature-256 header missing",
            )
        hash_object = hmac.new(
            self.token.encode("utf-8"), msg=payload, digestmod=hashlib.sha256
        )
        expected_signature = "sha256=" + hash_object.hexdigest()
        if not hmac.compare_digest(signature_header, expected_signature):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Request signatures invalid.",
            )


@router.post(path="/github", status_code=status.HTTP_204_NO_CONTENT)
async def github_webhook(request: Request, response: Response):
    headers = request.headers
    payload = await request.body()
    if payload:
        json_payload = json.loads(payload)
    try:
        wh = Webhook(security["token"])
        msg = wh.github_verify(payload, headers)
    except HTTPException as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return

    if json_payload["action"] == "push":
        update_json()
