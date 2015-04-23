import unittest
from .freenet.FreenetConnection import FreenetConnection


class TestFreeNetConnection(unittest.TestCase):

    def test_connection(self):
        connected = False
        try:
            freeCon = FreenetConnection()
            connected = True
        except:
            connected = False
        self.assertTrue(connected)

    def test_put_success(self):
        freeCon = FreenetConnection()
        uri = freeCon.put("this is my data")
        self.assertIsNotNone(uri)
        self.assertTrue("test_string" in uri)

    def test_get_success(self):
        freeCon = FreenetConnection()
        uri = freeCon.put("this is my data2")
        output = freeCon.get(uri)
        self.assertTrue(output == "this is my data")

suite = unittest.TestLoader().loadTestsFromTestCase(TestFreeNetConnection)
unittest.TextTestRunner(verbosity=2).run(suite)
