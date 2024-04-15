import bcrypt

from src.cfg.settings import security

TOKEN = security["token"]
hashed = bcrypt.hashpw(bytes(TOKEN, "utf-8"), bcrypt.gensalt())


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
