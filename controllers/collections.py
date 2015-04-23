import hashlib
from .models.collection_version import CollectionVersion
from .timestamp.timestampfile import TimestampFile
from .cache.cache import DBSession, Cache
import time
import datetime


def get_oldest(collection):
    """
    Used to get the latest timestamp time from collection
    :param collection:
    :return: oldest time
    """
    if collection.oldest_date is None:
        time_str = str(datetime.datetime.now()).split(".")[0]
        return time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    else:
        return collection.oldest_date


def get_latest(collection):
    """
    Used to get the latest timestamp time from collection
    :param collection:
    :return:latest time
    """
    if collection.oldest_date is None:
        return time.gmtime(0)
    else:
        get_time = collection.latest_btc_tx.split(";")
        return time.strptime(get_time[0], "%Y-%m-%d %H:%M:%S")


def edit_time(collection, curr, curr_txs):
    """
    Used to edit collection oldest_date, oldest_btc_tx, latest_btc_tx
    :param collection:
    :param curr: the new hash timestamp time
    :param curr_txs: new hash timestamp transaction id
    """
    oldest = get_oldest(collection)
    latest = get_latest(collection)
    if curr < oldest:
        collection.oldest_date = curr
        collection.oldest_btc_tx = curr_txs
    if curr > latest:
        collection.latest_btc_tx = curr_txs


def update_timestamp(collection):
    """
    Used to update collection timestamp information by new hash
    :param collection:
    """
    collection_version = collection.get_latest_collection_version()
    if(collection_version is None):
        print(
            "Timestamp called on empty collection, CollectionVersion not in Cache")
        return

    timestamp = TimestampFile(collection_version.root_hash).check_timestamp()
    curr_time = time.strptime(timestamp['time'], "%Y-%m-%d %H:%M:%S")
    curr_txs = timestamp['time'] + ";" + timestamp['Transaction']
    edit_time(collection, curr_time, curr_txs)


def update_hash(collection):
    string = ""
    if collection is None:
        return None
    # check whether the version hashed already collection.version
    for document in collection.documents:
        string += document.hash + "|"
        if len(string) == 0:
            return None
    string = string[:-1]
    h = hashlib.sha256()
    h.update(string)
    collection_hash = CollectionVersion(
        root_hash=h.hexdigest(), document_ids=string, collection_version=collection.get_latest_version() + 1,
        collection_address=collection.address)
    session = DBSession.object_session(collection)
    session.add(collection_hash)
    collection.version_list.append(collection_hash)
    session.commit()
