from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT = os.getenv('REDIS_PORT')
    REDIS_USERNAME = os.getenv('REDIS_USERNAME')
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
    
    REDIS_OM_URL = f"redis://@{REDIS_HOST}:{REDIS_PORT}"