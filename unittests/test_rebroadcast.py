import unittest
from controllers.controller import Controller
from models.collection import Collection
from models.keyword import Keyword
from models.document import Document
from models.signature import Signature
import hashlib
import uuid
import datetime
import time


class TestRebroadcast(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.address = self.controller.connection.create_address(
            'Controller Test address', True)

        coll_address = str(uuid.uuid1())
        doc_hash_1 = str(uuid.uuid1())
        doc_hash_2 = str(uuid.uuid1())
        doc_hash_3 = str(uuid.uuid1())

        self.test_collection = Collection(
            title="Test",
            description="This is a collection!",
            address=self.address,
            btc="123456789",
            keywords=[
                Keyword(name="Keyword A"),
                Keyword(name="Keyword B"),
            ],
            documents=[
                Document(
                    description="Test document A",
                    hash=doc_hash_1,
                    title="Test A",
                    accesses=0,
                    filename="joe.txt",
                    collection_address="afgagahhsgh"
                ),
                Document(
                    description="Test document B",
                    hash=doc_hash_2,
                    title="Test B",
                    accesses=3,
                    filename="gile.txt",
                    collection_address="afgagasghhhss"
                ),
            ],
            creation_date=datetime.datetime.now(),
            oldest_date=datetime.datetime.now(),
            latest_broadcast_date=datetime.datetime.now(),
            latest_btc_tx="btctx1",
            oldest_btc_tx="btctx12",
            accesses=2,
            votes=3,
            votes_last_checked=datetime.datetime.now()
        )
        self.test_signature = Signature(pubkey='itsakey', address=self.address)

    def tearDown(self):
        self.controller = None

    def test_rebroadcast(self):
        self.controller.cache.insert_new_collection(self.test_collection)
        self.test_signature.signature = hashlib.sha256(
            self.test_signature.pubkey + self.test_collection.to_json()).hexdigest()
        self.controller.cache.insert_new_collection(self.test_signature)
        result = self.controller.rebroadcast(
            self.test_collection, self.address, self.address)
        self.assertEqual(True, result)
