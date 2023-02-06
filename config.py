import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "26311402"))
    API_HASH = os.environ.get("API_HASH", "012450e57d2bc98d0693c6982d01a2d7")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5868897210:AAGLyP_LOHuX69N6SXYHG0QSgu5Ii7LZe5g")
    BOT_SESSION = os.environ.get("BOT_SESSION", "Autoforwardas_bot")
    OWNER_ID = os.environ.get("OWNER_ID", "5832887847")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Hacker:BREatMXQAWSX8Res@cluster0.0vrauzh.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Hacker")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQGReuoAULFN8zOauZ-fm7xbu4fdhkfRb61nPGFmVs5_Z5uZM_tFz1pFSIIJ8vm--KFXyPxht4SPs1CEZv4rAXOS3c3zbhzB2m04QuyzF1nvXZL2UQoDKXApcQK4rG_ge8pByi6Q-0FcqPyMwjF1mPcRP2mMyrKNoYhOYTQjaOcACoWgYQaqbooMvx4nozOUXTb21aFUyF91C6tBKzFit2DhWfBupSCp6QBrfs_BhicOSo5oVaqSo20Gxtn7kUC-Kn8crtmSPhXuhLnhJHf0q-cVBi9BwJz-gosARzafbL_lg6saOubCzFIX-pqS4V2bGPlMFLt6pQJVzYzX0HXqZzfOcgEizAAAAAFbqs4nAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001852600221"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Autoforwardas_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
