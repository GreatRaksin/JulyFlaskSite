import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'спорим_что_не_угадаешь'
