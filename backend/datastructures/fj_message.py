import datetime
import hashlib
import json
import os
import pwd
from backend.pyelliptic.arithmetic import *


class FJMessage():

    def __init__(self, type_id, original_sender, payload, pubkey=''):
        """
        FJMessage constructor. An FJMessage is any Free Journal bitmessage communication
        :param type_id: type of message being sent, 1=Collection, 2=Document, 3=Rebroadcast Request
        :param original_sender: the Bit Message address of the user sending this message
        :param payload: the content of this message
        :param pubkey: the public key associated with the bitmessage address of the payload
        """

        self.protocol = "FJ1.0"
        self.type_id = type_id
        self.original_sender = original_sender
        self.time_created = datetime.datetime.now()
        self.payload = payload
        self.pubkey = pubkey

    def _generate_signature(self):
        """
        Generates a sha256 signature of the public keys
        and the payload of the message
        """

        f = open('/home/'+pwd.getpwuid(os.getuid())[0]+'/.config/PyBitmessage/keys.dat', 'r')
        keys = f.read()
        keys_list = keys.split('\n\n')
        selected_key = []
        privkey_line = []

        for key_info in keys_list[1:]:
            if self.original_sender in key_info:
                selected_key = key_info.split('\n')

        for line in selected_key:
            if 'privsigningkey' in line:
                privkey_line = line.split('=')

        privkey = privkey_line[1].strip()
        public_signing_key = privtopub(privkey)
        self.pubkey = public_signing_key

        return hashlib.sha256(public_signing_key + self.payload).hexdigest()

    def to_json(self):
        """
        Creates a json encoding to be sendable in a Bit Message,
        :return: the json encoding of the message
        """
        signature = self._generate_signature()
        return json.dumps({"protocol": self.protocol, "type_id": self.type_id, "original_sender": self.original_sender,
                           "signature": signature, "time_created": self.time_created.strftime("%A, %d. %B %Y %I:%M%p"),
                           "payload": self.payload, "pubkey": self.pubkey}, sort_keys=True)
