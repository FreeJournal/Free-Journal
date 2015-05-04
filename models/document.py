from sqlalchemy import Column, ForeignKey, Integer, String
from models import DecBase


class Document(DecBase):

    """ A document represents a single document shared to the network.
        Documents are indexed by tuples contained in their respective collections.
        Documents are stored and retreived from the Freenet network using the hashes
        in the index, and if full caching is enables, are cached on disk according
        to their age and the number of accesses tracked on this node.

        Attributes:
            collection_address: The address of the Collection the document is contained in. @todo investigate multiple collections
            description: The description of the document as stored in the latest known DocIndex
            hash: The SHA-256 hash of this document
            title: The title of the document as stored in the latest known DocIndex
            filename: The document filename on disk, or None if not stored
            accesses: The number of accesses the document has received on the FreeJournal network
    """
    __tablename__ = 'document'
    collection_address = Column(String, ForeignKey('collection.address'))
    description = Column(String)
    hash = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    # Caching information (for pruning)
    filename = Column(String)
    accesses = Column(Integer, nullable=False, default=0)
