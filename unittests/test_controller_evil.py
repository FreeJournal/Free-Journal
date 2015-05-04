import unittest
from controllers.controller import Controller
from models.fj_message import FJMessage
from models.collection import Collection
from models.keyword import Keyword
from models.document import Document
import uuid
import datetime
import time


class TestControllerEvil(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()
        self.cache = self.controller.cache
        self.address = 'ffafaf'
        coll_address = str(uuid.uuid1())
        doc_hash_1 = str(uuid.uuid1())
        doc_hash_2 = str(uuid.uuid1())
        doc_hash_3 = str(uuid.uuid1())
        self.test_collection_evil = Collection(
            title="Test multiple33333",
            description="This is a collection! with multiple docs222",
            address=self.address,
            btc="123456789",
            keywords=[
                Keyword(name="Keyword A", id=1199),
                Keyword(name="Keyword c", id=1214),
            ],
            documents=[
                Document(
                    description="Test document Z",
                    hash="zzzzzzzz",
                    title="Test Z",
                    accesses=0,
                    filename="joe.txt",
                    collection_address="BM-2cSrapXpgDTFD8AyDmU1BGifNkB2Z6X9k8"
                ),
                Document(
                    description="Test document B",
                    hash='gdssgsdg',
                    title="Test B",
                    accesses=3,
                    filename="gile.txt",
                    collection_address="BM-2cSrapXpgDTFD8AyDmU1BGifNkB2Z6X9k8"
                ),
                Document(
                    description="Test document Bddd",
                    hash='afff',
                    title="Test B",
                    accesses=3,
                    filename="gile.txt",
                    collection_address="BM-2cSrapXpgDTFD8AyDmU1BGifNkB2Z6X9k8"
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

    def tearDown(self):
        self.controller = None

    def test_bad_signature(self):

        result = self.controller._check_signature(
            {'payload': 'afgga', 'signature': 'fake', 'pubkey': 'sff'})
        self.assertFalse(result)

    def test_address_not_in_keys(self):
        result = self.controller.publish_collection(
            self.test_collection_evil, self.address)
        self.assertFalse(result)

suite = unittest.TestLoader().loadTestsFromTestCase(TestControllerEvil)
unittest.TextTestRunner(verbosity=2).run(suite)
