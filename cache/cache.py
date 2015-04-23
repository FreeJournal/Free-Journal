from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import MetaData
from db import setup_db, connect_db
from .models.collection import Collection
from .models.document import Document
from .models.collection_version import CollectionVersion
from .models.keyword import Keyword

engine = connect_db()
setup_db(engine)
DBSession = sessionmaker(bind=engine)
meta = MetaData(bind=engine)


class Cache():

    """
    A Cache is an object used to communicate with the sqlalchemy database and store FreeJournal data locally

    Attributes:
        session: the sqlalchemy session for this Cache
    """

    def __init__(self):
        """
        Create a new database session to support
        insertion or removal of local data.
        """
        self.session = DBSession()

    def get_all_collections(self):
        """
        Get all collections currently stored locally
        :return: list of collections, ordered by date added
        """
        return self.session.query(Collection).order_by(Collection.creation_date.desc())

    def get_collection_with_address(self, address):
        """
        Retreive a specific collection as it's stored locally
        :param address: the collection BitMessage address to retreive
        :return: Collection object with desired ID in latest local state, or None if no matching Collection
        """
        row = None
        try:
            row = self.session.query(Collection).filter(
                Collection.address == address).one()
        except NoResultFound:
            pass
        return row

    def get_keyword_by_id(self, cur_id):
        """
        Retrieve a specific keyword by it's id
        :param cur_id: The id of the requested keyword
        :return: The Keyword object if in the cache, None otherwise
        """
        row = None
        try:
            row = self.session.query(Keyword).filter(
                Keyword.id == cur_id).one()
        except NoResultFound:
            pass
        return row

    def get_document_by_hash(self, hash):
        """
        Retrieve a specific Document by it's hash
        :param hash: The hash of the requested Document
        :return: The Document object if in the cache, None otherwise.
        """
        row = None
        try:
            row = self.session.query(Document).filter(
                Document.hash == hash).one()
        except NoResultFound:
            pass
        return row

    def get_documents_from_collection(self, collection_address):
        collections = self.session.query(Document).filter(
            Document.collection_address == collection_address).all()
        return collections

    def get_versions_for_collection(self, collection_address):
        versions = self.session.query(CollectionVersion).filter(
            CollectionVersion.collection_address == collection_address).all()
        return versions

    def insert_new_collection(self, collection):
        """
        Insert a new collection into local storage
        :param collection: Collection object to insert into local storage
        """
        self.session.add(collection)
        self.session.commit()

    # Note, if this is called manually(and not via cli/api) the collection
    # root hash will not be updated
    def insert_new_document(self, document):
        """
        Insert a new document associated with an existing collection into local storage
        :param document: Document object to insert into local storage
        """
        self.session.add(document)
        self.session.commit()

    def reset_database(self):
        """
        Drops all of the tables in the database.
        Currently this function is only used for unittesting.
        """
        meta.reflect()
        meta.drop_all()
        meta.create_all()

    def close(self):
        self.session.close()
