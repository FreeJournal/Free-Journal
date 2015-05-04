from controllers.controller import Controller
from bitmessage import Bitmessage
from config import MAIN_CHANNEL_ADDRESS
from cache.cache import Cache
from datetime import datetime


def rebroadcast(collection, testing_mode=False):
    """
    Rebroadcast the collection to the Main Channel
    :param collection: the collection object
    :return:
    """

    # Connect to bitmessage and create a temporary address
    bitmessage = Bitmessage()
    from_address = bitmessage.create_address("Rebroadcast", random=True)
    collection.address = from_address

    # Connect to controller and rebroadcast
    controller = Controller()
    print("Rebroadcasting collection: " + collection.title)

    if testing_mode:
        success = controller.publish_collection(collection, from_address, from_address)
    else:
        success = controller.publish_collection(collection, MAIN_CHANNEL_ADDRESS, from_address)

    if not success:
        return False

    return True


def find_old_collections(keepalive_constant, testing_mode=False):
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

            if testing_mode:
                success = rebroadcast(collection, testing_mode=True)
            else:
                success = rebroadcast(collection)

            if success:
                print("Updating collection in cache")
                cache.insert_new_collection(collection)
                counter += 1
            else:
                print("Sending rebroadcast failed")

    return counter
