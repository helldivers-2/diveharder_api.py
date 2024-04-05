from passlib.context import CryptContext
from diveharder.cfg.settings import security

SECRET_KEY = security["key"]
ALGORITHM = security["algorithm"]
TOKEN = security["token"]

pwd_context = CryptContext(schemes=["bcrypt"])


def verify_password(plain_password):
    return pwd_context.verify(plain_password, TOKEN)


def get_password_hash(password):
    return pwd_context.hash(password)
