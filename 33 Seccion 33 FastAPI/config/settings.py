import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    JWT_ALGORITHM: str = os.getenv('JWT_ALG')
    JWT_EXP_MINUTES: int = os.getenv('JWT_EXP_MINUTES')

settings = Settings()