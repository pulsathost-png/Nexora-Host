import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "nexora_secret_key")
DATABASE = "nexora.db"
