import unittest
from timestamp.timestampfile import TimestampFile


class TestTimestamp(unittest.TestCase):

    def test_connection(self):
        test_obj = TimestampFile(
            "444e6885f143a8b58b04c897f606b5ea826ff8aa42884f92e66d0a16ea0e29c8")
        value = test_obj.request_timestamp
        self.assertEqual(500000, value['price'])
        return 0

    def test_check(self):
        test_obj = TimestampFile(
            "783701f7599830824fa73488f80eb79894f6f14203264b6a3ac3f0a14012c25f")
        value = test_obj.check_timestamp()
        self.assertTrue(value['timestamp'])
        self.assertEqual(value['time'], "2015-03-01 06:42:08")
        self.assertEqual(
            value['Transaction'], "2be396b3c08c71c04e750142eda9216f52cdd4277345a239ec736fe2540f5e53")
        return 0

    def test_check_collection1(self):
        test_obj = TimestampFile(
            "f61504ae086c136511e7982c5d638a155c8a88832cd35c35c32f7de23ca5ce54")  # echo -n test_collection | sha256sum
        value = test_obj.check_timestamp()
        self.assertTrue(value['timestamp'])
        self.assertEqual(value['time'], "2015-03-16 02:19:19")
        self.assertEqual(
            value['Transaction'], "c6788150e4a409c653f7244da3ebfef3fa7cfb5faf87d3e31fd997d42bdfde7b")
        return 0


suite = unittest.TestLoader().loadTestsFromTestCase(TestTimestamp)
unittest.TextTestRunner(verbosity=2).run(suite)
