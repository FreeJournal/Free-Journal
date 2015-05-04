from cache.cache import Cache
from models.collection import Collection
from bitmessage.bitmessage_keepalive import find_old_collections
import datetime
import unittest


class TestKeepalive(unittest.TestCase):

    def setUp(self):
        cache = Cache()
        cache.reset_database()

        collection1 = Collection(
            title="First Collection",
            btc="btc",
            address="bm-first",
            description="description",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today(),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            latest_btc_tx="",
            oldest_btc_tx="",
            accesses=0,
            votes=0,
            votes_last_checked=datetime.datetime.today()
        )

        cache.insert_new_collection(collection1)

        collection2 = Collection(
            title="Second Collection",
            btc="btc",
            address="bm-second",
            description="description",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today() - datetime.timedelta(
                days=3),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            latest_btc_tx="",
            oldest_btc_tx="",
            accesses=0,
            votes=0,
            votes_last_checked=datetime.datetime.today()
        )

        cache.insert_new_collection(collection2)

        collection3 = Collection(
            title="Third Collection",
            btc="btc",
            address="bm-third",
            description="description",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today() - datetime.timedelta(
                days=1),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            latest_btc_tx="",
            oldest_btc_tx="",
            accesses=0,
            votes=0,
            votes_last_checked=datetime.datetime.today()
        )

        cache.insert_new_collection(collection3)

        collection4 = Collection(
            title="Fourth Collection",
            description="description",
            btc="btc",
            address="bm-fourth",
            keywords=[],
            documents=[],
            latest_broadcast_date=datetime.datetime.today() - datetime.timedelta(
                days=6),
            creation_date=datetime.datetime.today(),
            oldest_date=datetime.datetime.today(),
            latest_btc_tx="",
            oldest_btc_tx="",
            accesses=0,
            votes=0,
            votes_last_checked=datetime.datetime.today()
        )

        cache.insert_new_collection(collection4)

    def tearDown(self):
        cache = Cache()
        cache.reset_database()

    def test_bitmessage_keepalive(self):
        num_collections = find_old_collections(3, testing_mode=True)
        self.assertTrue(num_collections == 2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestKeepalive)
unittest.TextTestRunner(verbosity=2).run(suite)
