import os


class Config:
    SECRET = os.environ.get("SECRET", "")
