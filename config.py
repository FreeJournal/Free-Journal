""" URL to use for the SQLAlchemy engine.
    By default, the Postgres database is used and required.
    Feel free to change this to any of the commented, alternate
    URL's to change database management systems.
    DB_URL = 'postgres://postgres:password@localhost/freejournal'
    DB_URL = 'mysql://scott:tiger@localhost/foo'
"""
DB_URL = 'sqlite:///fj.db'

""" Caching strategy.
    'all': attempt to mirror all documents within diskspace constraints
    ('blacklist', [address array]):
    don't mirror collections on blacklist array
    ('whitelist', [address array]):
    don't mirror collections on blacklist array"""
# MIRROR_STRATEGY = ('blacklist', ['BM-1EXAMPLE'])
MIRROR_STRATEGY = 'all'

# Max disk space to use.  Allowable units are G and M.
MAX_DISKSPACE = '5G'

# Python command to start up the bitmessage daemon
RUN_PYBITMESSAGE_LINUX = \
    "python ~/PyBitmessage/src/bitmessagemain.py"

""" Proxy server address following
    http://<username>:<password>@0.0.0.0:<api-port>"""
BITMESSAGE_SERVER = \
    "http://username:password@0.0.0.0:8442/"

# Don't change this unless the main channel address is changed in the future
MAIN_CHANNEL_ADDRESS = "BM-2cWvQ4HqcxLhgKjc5zkuwsbqf69mryY5mr"
privsigningkey = "5JscnTKKubbtQepFUzFjKm9SjBMQ7PZKgd8EnauXZGwLjPVF2zs"
privencryptionkey = "5K9KRL9KffdbWcBqzPeXv5Rfo2YRJFD3SASJmXJsZkEphy4Rh6q"

""" Directory to store documents that are downloaded
(Make sure to keep the last '/' at the end of the path)"""
DOCUMENT_DIRECTORY_PATH = "~/Documents/"

# Set to true at your own risk
WEBAPP_DEBUG = True
WEBAPP_PORT = 5000
