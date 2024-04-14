import bcrypt

from src.cfg.settings import security

TOKEN = security["token"]
hashed = bcrypt.hashpw(bytes(TOKEN, "utf-8"), bcrypt.gensalt())


def verify_password(plain_password):
    if bcrypt.checkpw(str.encode(plain_password), hashed):
        return True
    else:
        return False
