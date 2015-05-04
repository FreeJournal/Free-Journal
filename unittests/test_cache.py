import unittest
import datetime
from models.collection import Collection
from models.document import Document
from models.keyword import Keyword
from cache.cache import Cache
from time import sleep
import uuid
import random


def create_test_collection(address):
    doc_hash_1 = str(uuid.uuid1())
    doc_hash_2 = str(uuid.uuid1())
    coll = Collection(
        title="Test",
        description="This is a collection!",
        address=address,
        btc="123456789",
        keywords=[
            Keyword(name=str(uuid.uuid1()), id=random.randint(0, 10000000)),
            Keyword(name=str(uuid.uuid1()), id=random.randint(0, 10000000)),
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
    return coll


class TestCache(unittest.TestCase):

    def setUp(self):
        self.cache = Cache()

    def tearDown(self):
        self.cache.session.rollback()

    def test_add_collection(self):
        coll_address = str(uuid.uuid1())
        coll = create_test_collection(coll_address)
        self.cache.session.add(coll)
        coll = self.cache.session.query(Collection).filter(
            Collection.address == coll_address).one()
        self.assertEquals(coll.title, "Test")
        doc = self.cache.session.query(Document).filter(Document.hash == coll.documents[1].hash).one()
        self.assertEquals(doc.title, "Test B")

    def test_pagination(self):
        addrs = [str(uuid.uuid1()) for _ in range(20)]
        for addr in addrs:
            coll = create_test_collection(addr)
            sleep(0.2)
            self.cache.session.add(coll)
        self.cache.session.commit()
        colls = self.cache.get_collections_paginated(3, 0)
        self.assertEquals(colls.count(), 3)
        self.assertEquals(colls[0].address, addrs[19])
        colls = self.cache.get_collections_paginated(5, 5)
        self.assertEquals(colls.count(), 5)
        self.assertEquals(colls[0].address, addrs[14])

suite = unittest.TestLoader().loadTestsFromTestCase(TestCache)
unittest.TextTestRunner(verbosity=2).run(suite)
