import os

# grab the folder where this scrip lives
basedir = os.path.abspath(os.path.dirname(__file__))
# print basedir

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = '\x07\x95\x15(\xf5~\xac\xa0\xdd^\x96#\x97\x0ew\xfb\x8e\x08`+2\x9a\x85\x0b'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
# print DATABASE_PATH

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
