import unittest
import datetime
from cache.cache import Cache
from models.collection import Collection
from models.document import Document
from models.keyword import Keyword
from controllers.collections import update_hash
from controllers import collections
import uuid
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.exc import StatementError

our_cache = Cache()


def add_collection():
    global our_cache
    coll_address = str(uuid.uuid1())
    doc_hash_1 = str(uuid.uuid1())
    doc_hash_2 = str(uuid.uuid1())
    coll = Collection(
        title="Test",
        description="This is a collection!",
        address=str(uuid.uuid1()),
        btc=str(uuid.uuid1()),
        keywords=[
        ],
        documents=[
            Document(
                collection_address=doc_hash_1,
                description="Test document A",
                hash=str(uuid.uuid1()),
                title="Test A",
            ),
        ],
        creation_date=datetime.datetime.now(),
        oldest_date=datetime.datetime.now(),
        latest_broadcast_date=datetime.datetime.now()
    )
    our_cache.insert_new_collection(coll)
    collections.update_hash(coll)
    our_cache.session.commit()
    return coll

param_arr = []
for i in range(0, 5):
    collection = add_collection()
    param_arr.append(
        ["update_hash_%d" % (i), collection, str(collection.get_latest_collection_version().root_hash)])


class TestSequense(unittest.TestCase):
    pass


def test_generator(test_coll, prev_value):
    def test(self):
        global our_cache
        with our_cache.session.no_autoflush:
            try:
                d = Document(
                    description=str(uuid.uuid4()),
                    hash=str(uuid.uuid4()),
                    collection_address=test_coll.address,
                    title=str(uuid.uuid4()),
                )
                our_cache.insert_new_collection(test_coll)
                our_cache.insert_new_document_in_collection(d, test_coll)
            except:
                # Test already ran
                return True
        collections.update_hash(test_coll)
        curr_value = test_coll.get_latest_collection_version().root_hash
        self.assertNotEqual(str(curr_value), prev_value)
    return test

for each_param in param_arr:
    test_name = 'test_%s' % each_param[0]
    test = test_generator(each_param[1], each_param[2])
    setattr(TestSequense, test_name, test)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequense)
    unittest.TextTestRunner(verbosity=2).run(suite)
