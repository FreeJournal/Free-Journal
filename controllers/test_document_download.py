import unittest
from backend.controller import Controller
from models.collection import Collection
from models.keyword import Keyword
from models.document import Document
import datetime
import time
from freenet.FreenetConnection import FreenetConnection
from config import MAIN_CHANNEL_ADDRESS, DOCUMENT_DIRECTORY_PATH
from bitmessage.bitmessage_listener import get_collections
import os


class TestDocumentDownload(unittest.TestCase):

    def test_get_document_invalid(self):
        controller = Controller()
        data = controller._get_document(
            "CHK@SjQPY2GVWNnkjTXse68DnE0u5WpH-sFHdpKHamFwAasdfasdj6UN~uJfBSQoSg8NEV6JsR-aPkCevDnSURvUnS9A")

        self.assertTrue(data == None)

    def test_save_document(self):
        controller = Controller()
        data = open('backend/Test1.txt', 'r').read()
        file_name = "Test1.txt"

        controller._save_document(data, file_name)
        self.assertTrue(
            os.path.exists(os.path.expanduser(DOCUMENT_DIRECTORY_PATH + "Test1.txt")))

    def test_get_document(self):
        controller = Controller()
        data = controller._get_document(
            "CHK@SjQPY2GVWNnkjTXse68DnE0u5WpH-sFHdpKHamFwA0U,IX8j6UN~uJfBSQoSg8NEV6JsR-aPkCevDnSURvUnS9A,AAMC--8")

        self.assertTrue(data != None)

    def test_config_path_exists(self):
        self.assertTrue(
            os.path.exists(os.path.expanduser(DOCUMENT_DIRECTORY_PATH)))

    def test_config_path_ending_slash(self):
        self.assertTrue(DOCUMENT_DIRECTORY_PATH[-1] == '/')


suite = unittest.TestLoader().loadTestsFromTestCase(TestDocumentDownload)
unittest.TextTestRunner(verbosity=2).run(suite)
