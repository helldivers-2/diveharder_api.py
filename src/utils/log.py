import logging
import sys
from typing import Optional

from fastapi import Request, status

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


def update_log_level(log_level):
    match log_level:
        case "DEBUG":
            logger.setLevel(logging.DEBUG)
        case "INFO":
            logger.setLevel(logging.INFO)
        case "WARNING":
            logger.setLevel(logging.WARNING)
        case "ERROR":
            logger.setLevel(logging.ERROR)
        case "CRITICAL":
            logger.setLevel(logging.CRITICAL)
        case _:
            logger.setLevel(logging.NOTSET)


def info(request: Request, response_status: status, user: str = ""):
    if user == "" or user is None:
        source = request.headers.get("User-Agent")
        user = "No User"
    else:
        source = user
    client = request.headers.get("x-super-client", False)
    client_type = "Super-Client" if client else "Client"
    super_contact = request.headers.get("x-super-contact", False)
    logger.debug(
        "Source: " + request.query_params.get("source", "No Source Param Specified")
    )
    logger.debug(
        "User-Agent: " + request.headers.get("User-Agent", "No User-Agent Found")
    )
    logger.info(
        f"[{request.headers.get('fly-client-ip', request.client.host)}] [{request.method} {request.url.path}] [{response_status}] [{client}] [Super Contact: {super_contact}]"
    )


def msg(message: Optional[str]):
    logger.info(msg="[" + str(message) + "]")


def error(message: Optional[str]):
    logger.debug(msg="[" + str(message) + "]")


def warn(message: Optional[str]):
    logger.warning(msg="[" + str(message) + "]")


def err(message: Optional[str]):
    logger.error(msg="[" + str(message) + "]")


def debug(message: Optional[str]):
    logger.debug(msg="[" + str(message) + "]")


def exception(message: Optional[str]):
    logger.exception(msg="[" + str(message) + "]")


def critical(message: Optional[str]):
    logger.critical(msg="[" + str(message) + "]")
