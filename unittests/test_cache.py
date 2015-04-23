import unittest
import datetime
from .models.collection import Collection
from .models.document import Document
from .models.keyword import Keyword
from .cache.cache import Cache
import uuid


class TestCache(unittest.TestCase):

    def setUp(self):
        self.cache = Cache()

    def tearDown(self):
        self.cache.session.rollback()

    def test_add_collection(self):
        coll_address = str(uuid.uuid1())
        doc_hash_1 = str(uuid.uuid1())
        doc_hash_2 = str(uuid.uuid1())
        coll = Collection(
            title="Test",
            description="This is a collection!",
            address=coll_address,
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
            oldest_date=datetime.datetime.now(),
            latest_broadcast_date=datetime.datetime.now()
        )
        self.cache.session.add(coll)
        coll = self.cache.session.query(Collection).filter(
            Collection.address == coll_address).one()
        self.assertEquals(coll.title, "Test")
        doc = self.cache.session.query(Document).filter(
            Document.hash == doc_hash_2).one()
        self.assertEquals(doc.title, "Test B")
        key = self.cache.session.query(
            Keyword).filter(Keyword.id == 90909090).one()
        self.assertEquals(key.name, "Keyword A")
        self.assertTrue(key in coll.keywords)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCache)
unittest.TextTestRunner(verbosity=2).run(suite)
