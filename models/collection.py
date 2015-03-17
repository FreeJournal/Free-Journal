from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Table
from sqlalchemy.orm import relationship
from models import DecBase
from models.document import Document
from models.keyword import Keyword
from jsonschema import *
from json_schemas import *
import json

# Define foreign keys required for joining defined tables together
keyword_association = Table('collection_keywords', DecBase.metadata,
                            Column('keyword_id', Integer, ForeignKey('keyword.id')),
                            Column('collection_address', String, ForeignKey('collection.address'))
                            )


class Collection(DecBase):
    """ A Collection is the fundamental unit of organization in the FreeJournal network.
        A Collection is a uniquely identifiable set of documents.  Each collection is associated
        with and signed by a BitMessage broadcast channel address.  Each collection contains
        a list of documents, a Bitcoin address for ranking, and a version.  Messages on the network
        called DocIndex messages share the state of a collection at a given version.

        This class stores the latest version of each collection the FreeJournal node decides to mirror.
        It also stores old timestamps and Merkle trees for bookkeeping purposes (@todo).

        Attributes:
            title: Title of collection (as in message spec)
            description: Collection description (as in message spec)
            merkle: Merkle hash of latest known version (as in message spec)
            address: Bitmessage address uniquely ID'ing collection (as in message spec)
            version: Current collection version (as in message spec)
            btc: Bitcoin address for rating documents (as in message spec)
            keywords: Keywords as list of Keyword class for searching (as in message spec)
            documents: List of document classes included in the collection (as in message spec)
            latest_broadcast_date: The date that this collection was last seen broadcasted in the Main Channel
            creation_date: Earliest known timestamp of collection, or if none earliest approximation of creation date of
                current version of collection
            oldest_date: Earliest known timestamp of collection, or if none earliest approximation of creation date of
                any version of collection
            latest_btc_tx: Latest Bitcoin transaction timestamping merkle belonging to this collection
            oldest_btc_tx: Oldest Bitcoin transaction timestamping merkle belonging to this collection
            accesses: Number of times this collection is accessed by a user of this node (for cache pruning)
            votes: Latest vote count from the Bitcoin network, used to rank collection
            votes_last_checked: Latest poll of Bitcoin network for collection votes, to coordinate internal repolling
    """
    __tablename__ = 'collection'
    title = Column(Text, nullable=False)
    description = Column(String)
    merkle = Column(String, nullable=False)
    address = Column(String, primary_key=True)
    version = Column(Integer)
    btc = Column(String)
    keywords = relationship(Keyword, secondary=keyword_association)
    documents = relationship(Document, cascade="all, delete-orphan")
    latest_broadcast_date = Column(DateTime, nullable=False)
    creation_date = Column(DateTime, nullable=False)
    oldest_date = Column(DateTime, nullable=False)
    latest_btc_tx = Column(String)
    oldest_btc_tx = Column(String)
    accesses = Column(Integer, nullable=False, default=0)
    votes = Column(Integer, nullable=False, default=0)
    votes_last_checked = Column(DateTime)

    def to_json(self):
        """
        Encodes a Collection as a json representation so it can be sent through the bitmessage network
        :return: the json representation of the given Collection
        """
        json_docs = []
        for doc in self.documents:
            json_docs.append({"address": doc.collection_address, "description": doc.description, "title": doc.title,
                              "hash": doc.hash, "filename": doc.filename, "accesses": doc.accesses})

        json_keywords = []
        for key in self.keywords:
            json_keywords.append({"id": key.id, "name": key.name})
        json_representation = {"type_id": 1,
                               "title": self.title,
                               "description": self.description,
                               "keywords": json_keywords,
                               "address": self.address,
                               "documents": json_docs,
                               "merkle": self.merkle,
                               "btc": self.btc,
                               "version": self.version,
                               "latest_broadcast_date": self.latest_broadcast_date.strftime("%A, %d. %B %Y %I:%M%p"),
                               "creation_date": self.creation_date.strftime("%A, %d. %B %Y %I:%M%p"),
                               "oldest_date": self.oldest_date.strftime("%A, %d. %B %Y %I:%M%p"),
                               "latest_btc_tx": self.latest_btc_tx,
                               "oldest_btc_tx": self.oldest_btc_tx,
                               "accesses": self.accesses,
                               "votes": self.votes,
                               "votes_last_checked": self.votes_last_checked.strftime("%A, %d. %B %Y %I:%M%p")}
        try:
            validate(json_representation, coll_schema)
            return json.dumps(json_representation, sort_keys=True)
        except ValidationError as m:
            return None

    def _keyword_in(self, key_id):
        """
        Finds if the given Keyword id is in the Collection's Keywords
        :param key_id: the Keyword id to search for
        :return: True if this id is in the Collection's Keywords, False otherwise
        """
        for key in self.keywords:
            if key.id == key_id:
                return True
        return False

    def update_keywords(self, new_keywords):
        """
        Updates the Collection's Keywords with any new Keywords in the given list.
        :param new_keywords: a list of Keywords
        """
        i = 0
        new_key_list = []
        while i < len(new_keywords):
            if not self._keyword_in(new_keywords[i].id):
                new_key_list.append(new_keywords[i])
            i += 1
        self.keywords.extend(new_key_list)

    def update_timestamp (self):
        """
        Updates the Collection's oldest_date, oldest_btc_tx, latest_btc_tx with any new timestamp.
        """
        timestamp_obj = TimestampFile(self.merkle)
        date_check = timestamp_obj.check_timestamp()
        curr_time = date_check['time']
        split_time = curr_time[0:4]+" "+curr_time[5:7]+" "+curr_time[8:10]+" "+curr_time[11:13]+" "+curr_time[14:16]+" "+curr_time[17:19]
        cmp_curr_time = time.strptime(split_time, "%Y %m %d %H %M %S")
        curr_txs= curr_time + ";" + date_check['Transaction']
        if self.oldest_date == None:
            self.oldest_date = cmp_curr_time
            self.oldest_btc_tx = curr_txs
            self.latest_btc_tx = curr_txs
            return
        split_time = self.latest_btc_tx.split(";")
        latest_time = split_time[0]
        latest_time_str = latest_time[0:4]+" "+latest_time[5:7]+" "+latest_time[8:10]+" "+latest_time[11:13]+" "+latest_time[14:16]+" "+latest_time[17:19]
        cmp_latest = time.strptime(latest_time_str, "%Y %m %d %H %M %S")
        if cmp_curr_time < self.oldest_date:
            self.oldest_date = cmp_curr_time
            self.oldest_btc_tx = curr_txs
        if cmp_curr_time > cmp_latest:
            self.latest_btc_tx = curr_txs
