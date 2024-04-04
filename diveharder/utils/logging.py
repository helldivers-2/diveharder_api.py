import logging
import sys
from fastapi import Request, status

# Get Logger
logger = logging.getLogger()

# Set logLevel
logLevel = logging.INFO

# Create Formatter
formatter = logging.Formatter(
    "[%(asctime)s] [7] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S %z"
)

# Create Handlers
stream_handler = logging.StreamHandler(sys.stdout)

# Set Formatter
stream_handler.setFormatter(formatter)

# Add Handles to Logger
logger.handlers = [stream_handler]

# Set log-level
logger.setLevel(logging.INFO)


def update_log_level(logLevel: int):
    match logLevel:
        case 10:
            logger.setLevel(logging.DEBUG)
        case _:
            logger.setLevel(logging.INFO)


def log(
    request: Request = None,
    status: status = None,
    message: str = None,
    user: str = "",
):
    source = request.headers.get("User-Agent", "")
    if user:
        source = user

    if request and status:
        logger.info(
            msg=f"[{request.client.host}:{request.client.port}] [{request.method} {request.url.path}] [{status}] [{source}]"
        )
    elif message:
        logger.info(msg="[" + str(message) + "]")


def debug(message: str):
    logger.debug(msg="[" + str(message) + "]")
