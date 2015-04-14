import unittest
from cache.cache import Cache
from controllers.collections import update_hash

collection = Cache().get_collection_with_address("BM-2cTicZFVNAyjzeRuP3okAJJnusty7YJQ2W")
param_arr = [[ "update_hash", collection, str(collection.hashes.first())]]

class TestSequense(unittest.TestCase):
    pass

def test_generator(test_coll, prev_value):
    def test(self):
        update_hash(test_coll)
        curr_value = test_coll.hashes.first()
        self.assertNotEqual(str(curr_value),prev_value)
    return test

for each_param in param_arr:
    for x in range(0, 3):
        test_name = 'test_%s' % each_param[0]
        test = test_generator(each_param[1], each_param[2])
        setattr(TestSequense, test_name, test)
        suite = unittest.TestLoader().loadTestsFromTestCase(TestSequense)
        unittest.TextTestRunner(verbosity=2).run(suite)

