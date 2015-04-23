from .controllers.controller import Controller
from .bitmessage import Bitmessage
from .config import MAIN_CHANNEL_ADDRESS
from .cache.cache import Cache
from datetime import datetime


def rebroadcast(collection):
    """
    Rebroadcast the collection to the Main Channel
    :param collection: the collection object
    :return: true if success, false if unsuccess
    """

    # Connect to bitmessage and create a temporary address
    bitmessage = Bitmessage()
    from_address = bitmessage.create_address("Rebroadcast", random=True)
    collection.address = from_address

    # Connect to controller and rebroadcast
    controller = Controller()
    print("Rebroadcasting collection: " + collection.title)

    success = controller.publish_collection(
        collection, MAIN_CHANNEL_ADDRESS, from_address)
    if not success:
        return False

    return True


def find_old_collections(keepalive_constant):
    """
    The main keep alive function that searches the cache
    for older collections that should be rebroadcasted to
    the Main Channel. This is to keep the network up-to-date.
    :param keepalive_constant: the age limit of a collection before it is rebroadcasted
    :return: the number of collections rebroadcasted
    """
    cache = Cache()
    collections = cache.get_all_collections()
    today = datetime.today()

    counter = 0
    for collection in collections:
        age = today - collection.latest_broadcast_date
        if age.days >= keepalive_constant:
            collection.latest_broadcast_date = datetime.today()
            success = rebroadcast(collection)

            if success:
                print("Updating collection in cache")
                cache.insert_new_collection(collection)
                counter += 1
            else:
                print("Sending rebroadcast failed")

    return counter
