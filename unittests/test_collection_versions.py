from cache.cache import Cache
from models.collection import Collection
from models.document import Document
from controllers import collections
import unittest
import datetime


class TestCollectionHistory(unittest.TestCase):

    def setUp(self):
        self.cache = Cache()
        self.cache.reset_database()
        self.collection1 = Collection(
            title="First Cdollection",
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
        self.cache.insert_new_collection(self.collection1)

    def test_two_doc_insert(self):
        d = Document(
            description="Test document A",
            hash="asdfasdfa;sldkfja;sldkfja;dljkfa;ldf",
            collection_address="bm-first",
            title="Test A",
        )
        d2 = Document(
            description="Test document B",
            hash="fdasdfsdfsdfsdfsdfsdfsdfdfsdfsddfdfdf",
            collection_address="bm-first",
            title="Test B",
        )
        self.cache.insert_new_document(d)
        collections.update_hash(self.collection1)
        self.cache.insert_new_document(d2)
        collections.update_hash(self.collection1)
        versions = self.cache.get_versions_for_collection(
            self.collection1.address)
        if(len(versions) < 2):
            print(len(versions))
            self.fail("No new version was created")
        self.assertTrue(len(versions) == 2)

    def test_empty_version(self):
        print("test")
        versions = self.cache.get_versions_for_collection(
            self.collection1.address)
        if(len(versions) != 0):
            self.fail("Version should be empty to start")

    def test_increment_collectionversion(self):
        versions = self.cache.get_versions_for_collection(
            self.collection1.address)
        if(len(versions) != 0):
            self.fail("Version should be nonzero")
        collections.update_hash(self.collection1)
        versions = self.cache.get_versions_for_collection(
            self.collection1.address)
        if(versions[0].collection_version != 1):
            self.fail("Incorrect collection version")

    def test_version_update(self):
        collections.update_hash(self.collection1)
        versions = self.cache.get_versions_for_collection(
            self.collection1.address)
        if(len(versions) != 1):
            self.fail("Version should be updated")
        if(versions[0].collection_address != self.collection1.address):
            print(versions[0].collection_address)
            print(self.collection1.address)
            self.fail("Wrong collection address")

    def test_different_root_hash(self):
        d = Document(
            description="Test document A",
            hash="asdfasdfa;sldkfja;sldkfja;dljkfa;ldf",
            collection_address="bm-first",
            title="Test A",
        )
        d2 = Document(
            description="Test document B",
            hash="fdasdfsdfsdfsdfsdfsdfsdfdfsdfsddfdfdf",
            collection_address="bm-first",
            title="Test B",
        )
        self.cache.insert_new_document(d)
        collections.update_hash(self.collection1)
        self.cache.insert_new_document(d2)
        collections.update_hash(self.collection1)
        versions = self.cache.get_versions_for_collection(
            self.collection1.address)
        self.assertTrue(versions[0].root_hash != versions[1].root_hash)

if __name__ == '__main__':
    unittest.main()
