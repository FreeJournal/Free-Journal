from config.config import *
import sys
import os


def process_collection(collection):
    """Cache the collection"""

    print("Retrieved a new collection!")
    print(collection.to_json())
    pass


def get_collections():
    """Get collections from the main channel"""

    collection_handler = CollectionHandler()
    new_collection = True
    while new_collection:
        new_collection = collection_handler.import_collection(MAIN_CHANNEL_ADDRESS)
        if new_collection:
            process_collection(new_collection)

if __name__ == '__main__':
    sys.path.append("..")
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(1, path)
    from collection_handler import CollectionHandler

    get_collections()