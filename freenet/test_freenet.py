import unittest
from FreenetConnection import FreenetConnection 

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
        uri = freeCon.put("test_string","this is my data")
        self.assertIsNotNone(uri)
        self.assertTrue("test_string" in uri)
   
    def test_get_success(self):
        freeCon = FreenetConnection()
        uri = freeCon.put("test_string","this is my data")
        output=freeCon.get(uri)
        self.assertTrue(output == "this is my data")
        




   


if __name__ == '__main__':
    unittest.main()    
