# from sqlalchemy import create_engine

class Config:
    # SECRET_KEY = 'n2020'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:0003@localhost:3308/sqlDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



# # config.py
# class Config:
#     # SECRET_KEY = 'n2020'
#     MYSQL_HOST = 'localhost'  # Utilisez votre adresse IP ici
#     MYSQL_USER = 'root'
#     MYSQL_PASSWORD = '0003'
#     MYSQL_DB = 'sqlDB'
#     MYSQL_PORT = 3308  # Le port correct
#     MYSQL_CURSORCLASS = 'DictCursor'
# # config.py
# class Config:
#     # SECRET_KEY = 'n2020'
#     MYSQL_HOST = '172.31.190.46'  # Utilisez votre adresse IP ici
#     MYSQL_USER = 'root'
#     MYSQL_PASSWORD = '0003'
#     MYSQL_DB = 'sqlDB'
#     MYSQL_PORT = 3308  # Le port correct
#     MYSQL_CURSORCLASS = 'DictCursor'

# import os

# class Config:
#     SECRET_KEY = 'n2020'
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:0003@localhost/myDB'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
# # config.py
