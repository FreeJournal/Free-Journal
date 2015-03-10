from global_imports import *

import json
import hashlib
import time
import base64


class CollectionHandler:

    def __init__(self):
        self.connection = Bitmessage()

    def _check_signature(self, fj_message, address):
        """
        Checks that the signature is the correct sha256 hash of the address and payload
        :param fj_message: the message containing the collection and signature
        :param address:  the address this collection came from
        :return: True if the signatures match, False otherwise
        """

        h = hashlib.sha256(fj_message["original_sender"] + fj_message['payload']).hexdigest()
        if h == fj_message["signature"]:
            print "Signature Verified"
            return True
        else:
            print "Signature Not Verified"
            return False

    def import_collection(self, address):
        """
        Imports a Collection from the given Bit Message address and checks if its signature is valid
        :param address: the address to import the collection from
        :return: A Collection object gathered from the Bit Message payload if successful,
        False otherwise
        """
        collections = []
        self.connection.subscribe(address)
        #buffer time to make sure to get messages
        time.sleep(10)
        messages = self.connection.check_inbox()
        for message in messages["inboxMessages"]:

            if message["fromAddress"] == address:

                #decoded_message is a FJMessage
                base64_decode = base64.b64decode(message["message"])
                try:
                    json_decode = json.loads(base64_decode)
                except (ValueError, TypeError):
                    print "Not a FJ Message or Invalid FJ Message"
                    continue

                #Trying to filter out non collection messages
                # TODO Change this filtering technique?
                if "payload" in json_decode and self._check_signature(json_decode, address):

                    payload = json_decode["payload"]
                    try:
                        payload = json.loads(payload)
                    except (ValueError, TypeError):
                        print "Contents of FJ Message invalid or corrupted"
                        continue

                    collections.append(Collection(payload["type_id"], payload["title"], payload["description"],
                                      payload["keywords"], payload["address"],
                                      payload["version"], payload["btc"], payload["documents"],
                                      payload["merkle"], payload["tree"]))

        if not collections:
            print "No Collections at this address"
            return False
        else:
            return collections


    def publish_collection(self, title, description, keywords, documents, address_label):
        """
        Creates a new collection and sends its Bit Message address to the main channel
        :param title: the title of the collection
        :param description: the description of the collection
        :param keywords: the keywords that apply to this collection
        :param documents: the FreeNet document addresses
        :param address_label: the label for the new Bit Message address
        :return: a new Collection object
        """
        new_address = self.connection.create_address(address_label)
        new_collection = Collection(1, title, description, keywords, new_address, 1, None, documents)
        collection_payload = new_collection.to_json()
        new_fj_message = FJMessage(1, new_address, collection_payload)
        new_fj_message.generate_signature()
        sendable_fj_message = new_fj_message.to_json()
        self.connection.send_message(MAIN_CHANNEL_ADDRESS, new_address, "New Collection - " + title, sendable_fj_message)
        self.connection.send_broadcast(new_address, "New Collection - " + title, sendable_fj_message)
        print "Address for this collection is", new_address
        return new_collection


