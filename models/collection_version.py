from sqlalchemy import Column, ForeignKey, Integer, String
from .models import DecBase


class CollectionVersion(DecBase):

    """
    A hash associated with a collection
    """
    __tablename__ = 'collection_version'
    collection_version = Column(Integer)
    root_hash = Column(String, primary_key=True)
    document_ids = Column(String)
    collection_address = Column(String, ForeignKey('collection.address'))
