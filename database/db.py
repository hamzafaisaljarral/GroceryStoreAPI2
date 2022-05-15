from mongoengine import connect

"""
To create connection with the mongo Db

"""


def initialize_db(app):
    connect(host=app.config['MONGODB_SETTINGS'])
