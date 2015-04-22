from datetime import timedelta

BROKER_URL = 'amqp://'

CELERYBEAT_SCHEDULE = {
    'listen': {
        'task': 'tasks.get_collections',
        'schedule': timedelta(seconds=30),
    },
    'test': {
        'task': 'tasks.test',
        'schedule': timedelta(seconds=10),
    }
}

CELERY_TIMEZONE = 'UTC'
