from celery import Celery

from controllers.controller import Controller
from config import MAIN_CHANNEL_ADDRESS


celery_app = Celery('tasks')
celery_app.config_from_object('tasks.celery_config')

@celery_app.task
def get_collections():
    """Get collections from the main channel"""
    collection_handler = Controller()
    collection_handler.import_collection(MAIN_CHANNEL_ADDRESS)

@celery_app.task
def test():
    pass

