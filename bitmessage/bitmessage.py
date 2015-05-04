import xmlrpclib
import subprocess
import os
import sys
from config import MAIN_CHANNEL_ADDRESS, BITMESSAGE_SERVER, RUN_PYBITMESSAGE_LINUX
import base64
import json


class Bitmessage():

    def __init__(self):
        self.os = sys.platform

        self.__startup()
        self.subscribe(MAIN_CHANNEL_ADDRESS, "FreeJournal Main Channel")

    def __startup(self):
        # Try connecting via the api first to see if PyBitmessage is already
        # running
        try:
            self._api_connect()
            assert(5 == self.api.add(2, 3))
        except:
            self._launch_bitmessage()
            self._api_connect()

        # Wait for api to connect to the bitmessage client
        connected = False
        while not connected:
            try:
                assert(5 == self.api.add(2, 3))
                connected = True
            except:
                pass

        self.api.connect()

        print('Connected successfully')

    def _api_connect(self):
        """Connect to the Bitmessage client
        """
        self.api = xmlrpclib.ServerProxy(BITMESSAGE_SERVER)

    def _launch_bitmessage(self):
        """Used to start up the PyBitmessage client so that we can connect to the api
        """
        print('Starting BitMessage on ' + self.os)
        if 'linux2' in self.os:
            # Used to ignore the ENORMOUS amount of output from PyBitmessage
            devnull = open(os.devnull, 'wb')

            # Start up PyBitmessage
            subprocess.Popen(
                [RUN_PYBITMESSAGE_LINUX], shell=True, stdout=devnull, stderr=devnull)

    def subscribe(self, address, label=None):
        """Subscribes to an address and gives it an optional label
        :param address: subscription bitmessage address
        :param label: (optional) text to associate with address
        :return boolean noting success of adding the subscription
        """
        # Retrieve a list of current subscriptions
        subs = self.api.listSubscriptions()

        # Ensure user isn't already subscribed to the address
        sub_dict = json.loads(subs)
        for sub in sub_dict["subscriptions"]:
            if sub['address'] == address:
                return False

        # Create subscription
        if label:
            encoded_label = base64.b64encode(label)
            self.api.addSubscription(address, encoded_label)
        else:
            self.api.addSubscription(address)

        return True

    def check_inbox(self, trash=False):
        """Returns a json object of all the messages currently in the user's inbox
        :param trash: boolean indicating whether the messages should be deleted (default is false)
        :return: json object of messages
        """
        messages = self.api.getAllInboxMessages()
        messages_dict = json.loads(messages)

        if trash:
            for message in messages_dict['inboxMessages']:
                self.delete_message(message['msgid'])

        return messages_dict

    def delete_message(self, message_id):
        self.api.trashMessage(message_id)

    def create_address(self, password, random=False):
        """Creates a deterministic address for the user
        :param password: text to use to create the deterministic address
        Will act as a label instead if random is set to True
        :param random: flag indicating whether the address should be deterministic
        or random (default is deterministic)
        :return: the bitmessage address
        """
        encoded_password = base64.b64encode(password)

        if random:
            return self.api.createRandomAddress(encoded_password)
        else:
            my_addresses = self.get_addresses()
            target_address = self.api.getDeterministicAddress(
                encoded_password, 3, 1)
            for address in my_addresses['addresses']:
                if address['address'] == target_address:
                    return target_address

            return json.loads(self.api.createDeterministicAddresses(encoded_password, 1, 3, 1))['addresses'][0]

    def get_addresses(self):
        """Get a list of addresses for the user
        :return: json object of the addresses
        """
        addresses = self.api.listAddresses2()
        addresses_dict = json.loads(addresses)

        return addresses_dict

    def get_sending_status(self, ack_data):
        return self.api.getStatus(ack_data)

    def send_message(self, to_address, from_address, subject, message):
        """Sends a message to specific address
        **Useful for communicating with the main channel**
        :param to_address: a valid address to send to
        :param from_address: a valid identity address
        :param subject: text
        :param message: text
        """

        encoded_subject = base64.b64encode(subject)
        encoded_message = base64.b64encode(message)
        ack_data = self.api.sendMessage(
            to_address, from_address, encoded_subject, encoded_message)

        print('Sending Message...')

        return ack_data

    def send_broadcast(self, from_address, subject, message):
        """Sends a broadcast to subscribers of the parameter address
        :param from_address: a valid address identity
        :param subject: text
        :param message: text
        """

        encoded_subject = base64.b64encode(subject)
        encoded_message = base64.b64encode(message)

        ack_data = self.api.sendBroadcast(
            from_address, encoded_subject, encoded_message)

        print('Sending Broadcast...')

        return ack_data
