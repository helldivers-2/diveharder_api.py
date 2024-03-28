import os
from dotenv import dotenv_values

env = "./.env" if os.path.isfile("./.env") else "./template.env"

api = dotenv_values(env)
