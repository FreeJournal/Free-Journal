from flask import Flask, render_template, send_from_directory, g
from .make_celery import make_celery
from datetime import timedelta
import datetime
from .cache.cache import Cache


app = Flask(__name__, static_folder='public')
app.config.update(
    CELERY_BROKER_URL='amqp://',
    CELERY_RESULT_BACKEND='amqp://',
    CELERYBEAT_SCHEDULE={
        'periodic_test': {
            'task': 'periodic_test',
            'schedule': timedelta(seconds=5),
            'args': (16, 16)
        },
    },
    CELERY_TIMEZONE='UTC'
)
celery = make_celery(app)


def get_cache():
    cache = getattr(g, '_cache', None)
    if cache is None:
        cache = g._cache = Cache()
    return cache


@app.teardown_appcontext
def teardown_cache(exception):
    cache = getattr(g, '_cache', None)
    if cache is not None:
        cache.close()


from .tasks.add_task import add_together
from .tasks.periodic_test import add_test

documents = [
    {
        "name": "Company, Inc. Hiring Practices",
        "type": "PDF",
        "keywords": ["corporate", "hiring", "leak"],
        "score": "1.243",
        "date": datetime.datetime.now(),
        "submitter": "wafflelover42"
    },
    {
        "name": "Company, Inc. Hiring Practices",
        "type": "PDF",
        "keywords": ["corporate", "hiring", "leak"],
        "score": "1.243",
        "date": datetime.datetime.now(),
        "submitter": "wafflelover42"
    },
    {
        "name": "Company, Inc. Hiring Practices",
        "type": "PDF",
        "keywords": ["corporate", "hiring", "leak"],
        "score": "1.243",
        "date": datetime.datetime.now(),
        "submitter": "wafflelover42"
    },
    {
        "name": "Company, Inc. Hiring Practices",
        "type": "PDF",
        "keywords": ["corporate", "hiring", "leak"],
        "score": "1.243",
        "date": datetime.datetime.now(),
        "submitter": "wafflelover42"
    },
]


@app.route('/')
def index():
    # TODO: Use Flask `g` object to store database connection
    return render_template("index.html", collections=get_cache().get_all_collections())


@app.route('/public/<path:path>')
def send_static(path):
    return send_from_directory('public', path)


@app.route('/celerytest')
def celery_test():
    result = add_together.delay(23, 42)
    return str(result.wait())
