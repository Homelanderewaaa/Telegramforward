import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "26311402"))
    API_HASH = os.environ.get("API_HASH", "012450e57d2bc98d0693c6982d01a2d7")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5868897210:AAGLyP_LOHuX69N6SXYHG0QSgu5Ii7LZe5g")
    BOT_SESSION = os.environ.get("BOT_SESSION", "Autoforwardas_bot")
    OWNER_ID = os.environ.get("OWNER_ID", "")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
