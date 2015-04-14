import unittest
import datetime
from models.collection import Collection
from models.document import Document
from models.keyword import Keyword
from controllers.collections import *
import uuid


class TestBitcoinIntegration(unittest.TestCase):

    def setUp(self):
        coll_address = str(uuid.uuid1())
        doc_hash_1 = str(uuid.uuid1())
        doc_hash_2 = str(uuid.uuid1())
        self.collection = Collection(
            title="Test",
            description="This is a collection!",
            merkle="f61504ae086c136511e7982c5d638a155c8a88832cd35c35c32f7de23ca5ce54",
            address=coll_address,
            version=1,
            btc="123456789",
            keywords=[
                Keyword(name="Keyword A", id=90909090),
                Keyword(name="Keyword B", id=91919191),
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
        )

    def test_update_collection(self):
        update_timestamp(self.collection)
        self.assertEqual(self.collection.latest_btc_tx, "2015-03-16 02:19:19;c6788150e4a409c653f7244da3ebfef3fa7cfb5faf87d3e31fd997d42bdfde7b")
        self.assertEqual(self.collection.oldest_btc_tx, "2015-03-16 02:19:19;c6788150e4a409c653f7244da3ebfef3fa7cfb5faf87d3e31fd997d42bdfde7b")

    def test_update_collection_older(self):
        update_timestamp(self.collection)
        self.collection.merkle =  "783701f7599830824fa73488f80eb79894f6f14203264b6a3ac3f0a14012c25f"
        update_timestamp(self.collection)
        self.assertEqual(self.collection.oldest_btc_tx, "2015-03-01 06:42:08;2be396b3c08c71c04e750142eda9216f52cdd4277345a239ec736fe2540f5e53")
        self.assertEqual(self.collection.latest_btc_tx, "2015-03-16 02:19:19;c6788150e4a409c653f7244da3ebfef3fa7cfb5faf87d3e31fd997d42bdfde7b")

    def test_update_collection_newer(self):
        self.collection.merkle =  "783701f7599830824fa73488f80eb79894f6f14203264b6a3ac3f0a14012c25f"
        update_timestamp(self.collection)
        self.collection.merkle =  "f61504ae086c136511e7982c5d638a155c8a88832cd35c35c32f7de23ca5ce54"
        update_timestamp(self.collection)
        self.assertEqual(self.collection.oldest_btc_tx, "2015-03-01 06:42:08;2be396b3c08c71c04e750142eda9216f52cdd4277345a239ec736fe2540f5e53")
        self.assertEqual(self.collection.latest_btc_tx, "2015-03-16 02:19:19;c6788150e4a409c653f7244da3ebfef3fa7cfb5faf87d3e31fd997d42bdfde7b")

suite = unittest.TestLoader().loadTestsFromTestCase(TestBitcoinIntegration)
unittest.TextTestRunner(verbosity=2).run(suite)

