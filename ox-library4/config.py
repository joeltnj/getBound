# config.py
class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'n2020'
    # SECRET_KEY = os.urandom(24) : ça c'est robuste
    SQLALCHEMY_DATABASE_URI =  'mysql://root:0003@localhost:3308/myDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
