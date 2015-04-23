from .bitmessage.bitmessage import Bitmessage
import unittest
import base64
import time


class TestBitmessage(unittest.TestCase):

    def setUp(self):
        try:
            self.bitmessage = Bitmessage()
        except:
            self.fail(
                "An exception was raised establishing a Bitmessage connection")

    def tearDown(self):
        self.bitmessage = None

    def test_create_address(self):
        label = "Test"
        encoded_label = base64.b64encode(label) + '\n'
        address = self.bitmessage.create_address(label, random=True)
        addresses = self.bitmessage.get_addresses()

        found = False
        for ad in addresses['addresses']:
            if encoded_label == ad['label'] and address == ad['address']:
                found = True
                break

        if not found:
            self.fail("Failed to create a new bitmessage address")

    def test_broadcast(self):
        message = "Hello World"
        subject = "Test Broadcast"
        address = self.bitmessage.create_address(
            "Unit Test: Broadcast", random=True)

        ack_data = self.bitmessage.send_broadcast(address, subject, message)

        timeout = 600  # 10 minutes
        start_time = time.time()
        curr_time = time.time()

        sent = False
        while curr_time - start_time < timeout:
            status = self.bitmessage.get_sending_status(ack_data)
            if 'sent' in status:
                sent = True
                break
            curr_time = time.time()
            time.sleep(3)

        if not sent:
            self.fail("Failed to send broadcast")

    def test_send_message(self):
        message = "Hello World"
        subject = "Test Message"
        address = self.bitmessage.create_address("Unit Test: Message")

        ack_data = self.bitmessage.send_message(address, address, subject, message)

        timeout = 600  # 10 minutes
        start_time = time.time()
        curr_time = time.time()

        sent = False
        while curr_time - start_time < timeout:
            status = self.bitmessage.get_sending_status(ack_data)
            if 'sent' in status:
                sent = True
                break
            curr_time = time.time()
            time.sleep(3)

        if not sent:
            self.fail("Failed to send message")

    def test_check_inbox(self):
        self.test_send_message()
        inbox = self.bitmessage.check_inbox(trash=True)
        self.assertTrue(len(inbox) >= 1)

suite = unittest.TestLoader().loadTestsFromTestCase(TestBitmessage)
unittest.TextTestRunner(verbosity=2).run(suite)
