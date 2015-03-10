import unittest
from backend.datastructures.fj_message import FJMessage


class TestFJMessage(unittest.TestCase):

    def setUp(self):
        self.test_fj_message = FJMessage(1, 'BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5', 'fake')

    def tearDown(self):
        self.test_fj_message = None

    def test_create_collection(self):
        self.assertIsInstance(self.test_fj_message, FJMessage)
        self.assertEqual(self.test_fj_message.type_id, 1)
        self.assertEqual(self.test_fj_message.original_sender, 'BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5')
        self.assertEqual(self.test_fj_message.payload, 'fake')

    def test_generate_signature(self):
        self.assertEqual(self.test_fj_message.signature, '')
        self.test_fj_message.generate_signature()
        self.assertEqual(self.test_fj_message.signature,
                         "c1c9edbf3e5d9ab913a62bfddcbf5e7ce3ed79a9edaed2de8c1d68924e24037b")
        self.test_fj_message.payload = 'notfake?'
        self.test_fj_message.generate_signature()
        self.assertEqual(self.test_fj_message.signature,
                         'e567b7ad070a48dc36fc35288297046e66721659c414e3221f60898c9094e79b')

    def test_to_json(self):
        test_json_encode = self.test_fj_message.to_json()
        self.assertIn('"original_sender": "BM-2cXbNb5UVcZndcQL6yrhm1iceGyX1KDKK5", "payload": "fake", '
                      '"protocol": "FJ1.0", "signature": ""', test_json_encode,)


suite = unittest.TestLoader().loadTestsFromTestCase(TestFJMessage)
unittest.TextTestRunner(verbosity=2).run(suite)
