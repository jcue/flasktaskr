import od

# grab the folder where this scrip lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSOWRD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = '\x07\x95\x15(\xf5~\xac\xa0\xdd^\x96#\x97\x0ew\xfb\x8e\x08`+2\x9a\x85\x0b'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)