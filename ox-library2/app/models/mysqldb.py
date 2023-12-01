# # app/models/mysqldb.py

# from flask import current_app
# from flask_mysqldb import MySQL

# mysql = MySQL()

# def init_app(app):
#     mysql.init_app(app)

# def get_db():
#     return mysql.connection

# def query_db(query, args=(), one=False):
#     cur = get_db().cursor()
#     cur.execute(query, args)
#     rv = cur.fetchall()
#     cur.close()
#     return (rv[0] if rv else None) if one else rv

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
