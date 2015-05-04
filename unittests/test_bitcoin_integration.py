import unittest
import datetime
from cache.cache import Cache
from models.collection import Collection
from controllers.collections import update_timestamp_version
from models.document import Document
from models.keyword import Keyword
from controllers import collections
import uuid



class TestBitcoinIntegration(unittest.TestCase):

    def setUp(self):
        self.our_cache = Cache()

    def add_collection(self):
        our_cache = self.our_cache
        coll_address = str(uuid.uuid1())
        doc_hash_1 = str(uuid.uuid1())
        doc_hash_2 = str(uuid.uuid1())
        coll = Collection(
            title="Test",
            description="This is a collection!",
            address=coll_address,
            btc="123456789",
            keywords=[
            ],
            documents=[
                Document(
                    description="Test document A",
                    hash=doc_hash_1,
                    title="Test A",
                ),
                Document(
                    description="Test document B",
                    hash=doc_hash_2,
                    title="Test B",
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

    def test_update_collection(self):
        our_cache = self.our_cache
        collection = self.add_collection()
        collection_version = collection.get_latest_collection_version()
        collection_version.root_hash = "f61504ae086c136511e7982c5d638a155c8a88832cd35c35c32f7de23ca5ce54"
	collections.update_timestamp_version(collection, collection_version)

        self.assertEqual(collection.latest_btc_tx, "2015-03-16 02:19:19;c6788150e4a409c653f7244da3ebfef3fa7cfb5faf87d3e31fd997d42bdfde7b")
        self.assertEqual(collection.oldest_btc_tx, "2015-03-16 02:19:19;c6788150e4a409c653f7244da3ebfef3fa7cfb5faf87d3e31fd997d42bdfde7b")

    def test_update_collection_older(self):
        our_cache = self.our_cache
        collection = self.add_collection()
        collection_version = collection.get_latest_collection_version()
        collection_version.root_hash = "783701f7599830824fa73488f80eb79894f6f14203264b6a3ac3f0a14012c25f"
	collections.update_timestamp_version(collection, collection_version)

        self.assertEqual(collection.oldest_btc_tx, "2015-03-01 06:42:08;2be396b3c08c71c04e750142eda9216f52cdd4277345a239ec736fe2540f5e53")
        self.assertEqual(collection.latest_btc_tx, "2015-03-01 06:42:08;2be396b3c08c71c04e750142eda9216f52cdd4277345a239ec736fe2540f5e53")

suite = unittest.TestLoader().loadTestsFromTestCase(TestBitcoinIntegration)
unittest.TextTestRunner(verbosity=2).run(suite)
