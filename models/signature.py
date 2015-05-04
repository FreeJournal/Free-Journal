from sqlalchemy import Column, ForeignKey, Integer, String
from models import DecBase


class Signature(DecBase):

    """ A signature validates the contents of a collection.

        Attributes:
            id: The unique identifier for a signature
            pubkey: the Bitmessage pubkey associated with this signature
            signature: the SHA256 hash of the pubkey and the contents of the associated collection
            address: the Bitmessage address that this signature is for

    """
    __tablename__ = 'signature'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pubkey = Column(String)
    signature = Column(String)
    address = Column(String, ForeignKey('collection.address'))
