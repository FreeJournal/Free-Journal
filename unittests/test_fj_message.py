import unittest

from models.fj_message import FJMessage
from config import MAIN_CHANNEL_ADDRESS


class TestFJMessage(unittest.TestCase):

    def setUp(self):
        self.test_fj_message = FJMessage(1, MAIN_CHANNEL_ADDRESS, 'fake')

    def tearDown(self):
        self.test_fj_message = None

    def test_create_collection(self):
        self.assertIsInstance(self.test_fj_message, FJMessage)
        self.assertEqual(self.test_fj_message.type_id, 1)
        self.assertEqual(
            self.test_fj_message.original_sender, MAIN_CHANNEL_ADDRESS)
        self.assertEqual(self.test_fj_message.payload, 'fake')

    def test_generate_signature(self):
        # test_json_encode = self.test_fj_message.to_json()
        # self.assertIn('"signature": "f4994f369c207566f49d149119169b34462833e4324c73510dd2823289edef72"',
        #              test_json_encode)
        # self.test_fj_message.payload = 'notfake?'
        # test_json_encode = self.test_fj_message.to_json()
        # self.assertIn('"signature": "ecd78830a89d58d3fc8529247788654158d4f4917fd590918cc944e7ea7b8fc3"',
        #                 test_json_encode)
        pass

    def test_to_json(self):
        # test_json_encode = self.test_fj_message.to_json()
        # self.assertIn('"original_sender": "BM-2cWvQ4HqcxLhgKjc5zkuwsbqf69mryY5mr", "payload": "fake", "protocol": "FJ1.0", '
        #              '"pubkey": "04ea42d4b855e2cf87f9227269542c29e789fadabbaaac893a59e84f48d8e801b6e906488a3196b3e722e6f38623ef57fe505f4f38038b530371f89b03b81a07ce',
        #              test_json_encode)
        pass


suite = unittest.TestLoader().loadTestsFromTestCase(TestFJMessage)
unittest.TextTestRunner(verbosity=2).run(suite)
