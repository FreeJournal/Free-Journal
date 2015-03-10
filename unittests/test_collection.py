import unittest
from backend.datastructures.collection import Collection


class TestCollection(unittest.TestCase):

    def setUp(self):
        type_id = 1
        title = 'title'
        description = 'description'
        keywords = ['keyword1', 'keyword2', 'keyword3']
        collection_address = 'BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5'
        version = 1
        btc = 'BC-241'
        documents = [('hash1', 'title1', 'description1'), ('hash2', 'title2', 'description2'),
                     ('hash3', 'title3', 'description3')]
        merkle = None
        tree = None
        self.test_collection = Collection(type_id, title, description, keywords, collection_address,
                                          version, btc, documents, merkle, tree)

    def tearDown(self):
        self.test_collection = None

    def test_create_collection(self):
        self.assertIsInstance(self.test_collection, Collection)
        self.assertEqual(self.test_collection.type_id, 1)
        self.assertEqual(self.test_collection.title, 'title')
        self.assertEqual(self.test_collection.description, 'description')
        self.assertEqual(self.test_collection.keywords[1], 'keyword2')
        self.assertEqual(self.test_collection.collection_address, 'BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5')
        self.assertEqual(self.test_collection.version, 1)
        self.assertEqual(self.test_collection.btc, 'BC-241')
        self.assertEqual(self.test_collection.documents[0], ('hash1', 'title1', 'description1'))
        self.assertIsNone(self.test_collection.merkle)
        self.assertIsNone(self.test_collection.tree)
        self.assertEqual(self.test_collection.documents[2][1], 'title3')

    def test_add_document(self):
        test_document = ('hash new', 'title new', 'description new')
        self.test_collection.add_document(test_document)
        self.assertEqual(self.test_collection.documents[-1], test_document)

    def test_to_json(self):
        test_json = self.test_collection.to_json()
        self.assertEqual(test_json, '{"address": "BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5", "btc": "BC-241", '
                                    '"description": "description", "documents": [["hash1", "title1", "description1"], '
                                    '["hash2", "title2", "description2"], ["hash3", "title3", "description3"]], '
                                    '"keywords": ["keyword1", "keyword2", "keyword3"], '
                                    '"merkle": null, "title": "title", "tree": null, "type_id": 1, '
                                    '"version": 1}')

suite = unittest.TestLoader().loadTestsFromTestCase(TestCollection)
unittest.TextTestRunner(verbosity=2).run(suite)
