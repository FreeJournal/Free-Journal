from .models.keyword import Keyword
from .models.document import Document
from .models.collection import Collection
from .bitmessage.bitmessage import Bitmessage
from .models.fj_message import FJMessage
from .cache.cache import Cache
from .config import DOCUMENT_DIRECTORY_PATH
from .freenet.FreenetConnection import FreenetConnection
from jsonschema import *
from .models.json_schemas import *
from sqlalchemy.exc import IntegrityError
from random import randint
import json
import time
import base64
import datetime
import hashlib
import thread
import sys
import os


class Controller:

    def __init__(self):
        self.connection = Bitmessage()
        self.cache = Cache()

    def _check_signature(self, fj_message):
        """
        Checks that the signature is the correct sha256 hash of the address's public keys and payload
        :param fj_message: the message containing the collection and signature
        :return: True if the signatures match, False otherwise
        """
        h = hashlib.sha256(
            fj_message["pubkey"] + fj_message['payload']).hexdigest()

        if h == fj_message["signature"]:
            print "Signature Verified"
            return True
        else:
            print "Signature Not Verified"
            return False

    def _build_docs_keywords(self, payload):
        """
        Builds a list of Keyword objects and a list of Document objects from the received json.

        :param payload: The payload of the FJ Message including the documents and keywords
        :return: Two lists representing the documents and keywords of the FJ Message
        """
        keywords = []
        docs = []
        for key in payload["keywords"]:
            db_key = self.cache.get_keyword_by_id(key["id"])
            if db_key is not None:
                keywords.append(db_key)
            else:
                keywords.append(Keyword(name=key["name"], id=key["id"]))

        for doc in payload["documents"]:
            db_doc = self.cache.get_document_by_hash(doc["hash"])
            if db_doc is not None:
                docs.append(db_doc)
            else:
                docs.append(
                    Document(
                        collection_address=doc[
                            "address"], description=doc["description"],
                        hash=doc["hash"], title=doc["title"]))
        return docs, keywords

    def _save_document(self, data, file_name):
        """
        Private helper function for writing file data to disk.
        Creates the file to the directory specified in config.py.

        :param data: the file data
        :param file_name: the name of the file
        :return: a boolean indicating success
        """

        try:
            file_path = os.path.expanduser(DOCUMENT_DIRECTORY_PATH) + file_name
            open(file_path, 'w').write(data)
            return True
        except Exception as e:
            return False

    def _get_document(self, hash):
        """
        Private helper function for getting document data
        from freenet.

        :param hash: the Content Hash Key for a document
        :return: the file data if successful, None otherwise
        """

        data = None

        # Try obtaining a freenet connection
        try:
            freenet_connection = FreenetConnection()
        except Exception as e:
            print("Couldn't connect to freenet")
            return data

        try:
            data = freenet_connection.get(hash)
        except Exception as e:
            pass

        return data

    def _hash_document_filenames(self, documents):
        """
        Private helper function for hashing a collection of
        documents file names so that file name conflicts will be
        rare.

        :param documents: a list of document objects
        """

        for document in documents:
            # Create a new file name out of a hash to deal with possible naming
            # conflicts
            file_name = document.filename
            if not document.filename:
                file_name = document.title + str(randint(0, 100))

            name, extension = os.path.splitext(file_name)
            hash_name = hashlib.sha256(name + str(randint(0, 100))).hexdigest()
            new_file_name = hash_name + extension

            # Save the new file name to the cache so it can be viewed later
            document.filename = new_file_name
            self.cache.insert_new_document(document)

    def _download_documents(self, collection_title, documents):
        """
        A function that downloads documents from a collection.
        NOTE: This function should only be called in its own thread
        since this is a blocking call and can take awhile to execute.

        :param collection_title: the title of the collection
        :param documents: the list of document objects to download
        """

        print("Downloading documents for " + collection_title)
        print("Number of Documents to download: " + str(len(documents)))

        doc_counter = 0
        for document in documents:
            # Store and validate that the document has a file name
            file_name = document.filename
            if not file_name:
                file_name = collection_title + str(doc_counter)
                doc_counter += 1

            # Try obtaining the file data from freenet
            data = self._get_document(document.hash)
            if not data:
                print("Couldn't download " + file_name + " from freenet")
                continue

            # If the file data was successfully downloaded, save the data to
            # disk
            success = self._save_document(data, file_name)
            if success:
                print("Successfully downloaded " + file_name + " from freenet")
            else:
                print("Couldn't save document data to disk (check that the document"
                      + " directory path exists and appropriate permissions are set")

        sys.exit()  # Exit current thread

    def _cache_collection(self, message, payload):
        """
        Checks to see if this collection is already in the cache. If it is we update the collection with the new data.
        Otherwise a new collection is made and cached.
        :param message: the Bitmessage message containing an FJ_message
        :param payload: the contents of the FJ_message
        """
        # Grabbing the text representations of the documents and keywords and
        # rebuilding them
        docs, keywords = self._build_docs_keywords(payload)
        cached_collection = self.cache.get_collection_with_address(
            payload["address"])

        if cached_collection is None:
            collection_model = Collection(
                title=payload["title"],
                description=payload["description"],
                address=payload["address"],
                btc=payload["btc"],
                keywords=keywords,
                documents=docs,
                creation_date=datetime.datetime.strptime(
                    payload["creation_date"], "%A, %d. %B %Y %I:%M%p"),
                oldest_date=datetime.datetime.strptime(
                    payload["oldest_date"], "%A, %d. %B %Y %I:%M%p"),
                latest_broadcast_date=datetime.datetime.strptime(
                    payload["latest_broadcast_date"], "%A, %d. %B %Y %I:%M%p"),
                votes=payload['votes'],
                votes_last_checked=datetime.datetime.strptime(
                    payload["votes_last_checked"], "%A, %d. %B %Y %I:%M%p"),
            )
            try:
                self.cache.insert_new_collection(collection_model)
                self._hash_document_filenames(collection_model.documents)
                thread.start_new_thread(self._download_documents, (
                    collection_model.title, collection_model.documents))
                print "Cached New Collection"
                return True
            except IntegrityError as m:
                print m.message
                return False
        else:
            cached_collection.keywords = keywords
            cached_collection.title = payload["title"]
            cached_collection.description = payload["description"]
            cached_collection.address = payload["address"]
            cached_collection.btc = payload["btc"]
            cached_collection.documents = docs
            cached_collection.creation_date = datetime.datetime.strptime(
                payload["creation_date"],
                "%A, %d. %B %Y %I:%M%p")
            cached_collection.oldest_date = datetime.datetime.strptime(
                payload["oldest_date"], "%A, %d. %B %Y %I:%M%p")
            cached_collection.latest_broadcast_date = datetime.datetime.strptime(
                payload["latest_broadcast_date"],
                "%A, %d. %B %Y %I:%M%p")
            cached_collection.votes = payload['votes']
            cached_collection.votes_last_checked = datetime.datetime.strptime(
                payload["votes_last_checked"], "%A, %d. %B %Y %I:%M%p")
            try:
                self.cache.insert_new_collection(cached_collection)
                self._hash_document_filenames(cached_collection.documents)
                thread.start_new_thread(self._download_documents, (
                    cached_collection.title, cached_collection.documents))
                print "Cached Updated Collection"
                return True
            except IntegrityError as m:
                print m.message
                return False

    def _find_address_in_keysdat(self, address):
        """
        Checks if this bitmessage address is in our keys.dat
        :param address: The address to look for
        :return: True if the address is in keys.dat, false otherwise
        """
        f = open(os.path.expanduser('~/.config/PyBitmessage/keys.dat'), 'r')
        keys = f.read()
        keys_list = keys.split('\n\n')

        for key_info in keys_list[1:]:
            if address in key_info:
                return True
        return False

    def import_collection(self, address):
        """
        Imports a Collection from the given Bit Message address and checks if its signature is valid.
        If it is valid then it is cached locally.
        :param address: the address to import the collection from
        :return: True if the collection was imported and cached successfully, False otherwise
        """

        # buffer time to make sure to get messages
        time.sleep(10)
        messages = self.connection.check_inbox()
        for message in messages["inboxMessages"]:
            if message["toAddress"] == address:
                # decoded_message is a FJMessage
                base64_decode = base64.b64decode(message["message"])
                try:
                    json_decode = json.loads(base64_decode)
                    validate(json_decode, fj_schema)
                except (ValueError, TypeError, ValidationError) as m:
                    # print m.message
                    print "Not a FJ Message or Invalid FJ Message"
                    self.connection.delete_message(message['msgid'])
                    continue

                # Trying to filter out non collection messages
                # TODO Change this?
                if "payload" in json_decode:
                    payload = json_decode["payload"]
                    try:
                        payload = json.loads(payload)
                        validate(payload, coll_schema)
                    except (ValueError, TypeError, ValidationError) as m:
                        print "Contents of FJ Message invalid or corrupted"
                        self.connection.delete_message(message['msgid'])
                        continue

                    if self._check_signature(json_decode):
                        if self._cache_collection(message, payload):
                            self.connection.delete_message(message['msgid'])
                            return True

        # print "Could not import collection"
        return False

    def publish_collection(self, collection, to_address, from_address=None):
        """
        Publishes the given to collection to the bitmessage network
        :param collection: the collection to be published
        :param to_address: the address to send the collection to,  always MAIN_CHANNEL_ADDRESS except in unittests
        :param from_address: the address to send the collection from
        :return: True if the collection is published successfully, False otherwise
        """

        if from_address is None:
            from_address = self.connection.create_address("new address")
            print "created address: ", from_address
        if not self._find_address_in_keysdat(from_address):
            print "This address is not in keys.dat, can not send message"
            return False

        collection_payload = collection.to_json()
        if collection_payload is None:
            return False
        new_fj_message = FJMessage(1, collection.address, collection_payload)
        sendable_fj_message = new_fj_message.to_json()
        if sendable_fj_message is None:
            return False
        self.connection.send_message(
            to_address, from_address, "subject", sendable_fj_message)
        return True
