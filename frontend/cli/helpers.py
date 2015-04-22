import sys
import datetime
import platform

# BitMessage installer imports
from bitmessage.install import apt_install, windows_install

# FreeNet installer imports
from freenet.install import linux_install

from tasks.install import rabbitmq_install

try:
    from controllers import collections
except:
    print('SQLAlchemy import error')

# FreeJournal library imports
import config
try:
    from cache.cache import Cache
    cache = Cache()
except:
    print ("Warning: SQLite is not installed.  No local cache " \
           + "functionality available.")

try:
    from models.collection import Collection
    from models.keyword import Keyword
    from models.document import Document
except:
    print ("Error: could not import models.")

try:
    from bitmessage.bitmessage import Bitmessage
    from controllers.controller import Controller
except:
    print ("Error: could not import BitMessage dependencies.")


try:
    # Freenet may not be installed
    import freenet
    from freenet.FreenetConnection import FreenetConnection
    freenet_installed = True
except:
    freenet_installed = False


def get_doc_file(document_hash, document_output_filename):
    """ Get a document file from the Freenet network
        :param document_hash: the Freenet URI to retreive
        :param document_output_filename: path/filename to write to
    """
    free_conn = FreenetConnection()
    output = free_conn.get(document_hash)
    open(document_output_filename, 'w').write(output)
    print ("File with URL " + document_hash + " written to " + document_output_filename)


def list_collections():
    """ List all collections in the local cache """
    print ("Available collections, cached locally: ")
    for collection in cache.get_all_collections():
        print ("\n\tID " + collection.address + "\t " + collection.title + \
               "\tCreation Date " + collection.creation_date.strftime("%A, %d. %B %Y %I:%M%p"))
        print ("\t" +"~~~~~~~~~~~~~~~Document list~~~~~~~~~~~~~~~")
        print ("\t\t" + "URI" + "\t" + "Title" + "\t" + "Description")
        documents = cache.get_documents_from_collection(collection.address)
        for doc in documents:
            print ("\t\t" + doc.hash + "\t" + doc.title +  "\t" + doc.description)


def list_collection_details(collection_address):
    collection = cache.get_collection_with_address(collection_address)
    if collection is not None:
        print (collection.to_json())
    else:
        print ("Collection not found in local cache.")


def list_collection_version(collection_address, show_document_ids):
    versions = cache.get_versions_for_collection(collection_address)
    if(len(versions)!=0):
        print("Collection Versions for " + collection_address + ":" )
        print ("\t" + "Root hash" + "\t\t\t\t\t\t\t\t" + "Collection Version")
    else:
        print("Collection not found")
    for version in versions:
        print("\t" + version.root_hash + "\t" + str(version.collection_version))
        if show_document_ids:
            print("document_ids:")
            print(version.document_ids)
            print("")


def install_dependencies(dependency):
    """ Install a prerequisite (dependency) for deploying a FreeJournal
        node.  Rerun with each FreeJournal upgrade.
        :param dependency: Software to install, freenet/bitmessage/all
    """
    if dependency == 'freenet' or dependency == 'all':
        os = sys.platform
        if 'linux' not in os:
            raise Exception("Invalid Operating System. See README.")
        else:
            linux_install()
    if dependency == 'rabbitmq' or dependency == 'all':
        os = sys.platform
        if 'linux' not in os:
            raise Exception("Invalid Operating System. See README.")
        else:
            rabbitmq_install()
    if dependency == 'bitmessage' or dependency == 'all':
        os_version = platform.dist()[0]
        if 'windows' in os_version:
            windows_install()
        else:
            apt_install()
            print ('Installation Completed')


def put_document(file_path, collection_address, title, description):
    """ Insert a document into the local cache with associated information
        and upload the document to the freenet network.
        :param file_path: the path of the file to upload
        :param collection_address: the collection address associated with the document
        :param title: the title of the document being uploaded
        :param description: the description of the document being uploaded
    """
    file_name = file_path.rsplit('/',1)[0]
    contents = open(file_path).read()
    free_conn = FreenetConnection()
    uri = free_conn.put(contents)
    document = Document(
        collection_address=collection_address,
        description=description,
        hash=uri,
        title=title,
        filename=file_name,
        accesses=0
    )
    cache.insert_new_document(document)
    collection = cache.get_collection_with_address(collection_address)
    collections.update_hash(collection)
    print ("Inserted " + file_path + " successfully with URI " + uri)
    print ("Allow up to 10 minutes for file to propogate on the freenet network")

def put_collection(address_password, title, description, keywords, btc):
    """ Create a collection in local cache
        :param address_password: The password with which to protect the collection.
        Should be at least 20 characters for optimal security and unique.  Generates 
        the unique collection ID deterministically
        :param title: The title of the created collection
        :param description: The description of the created collection
        :param keywords: Comma-separated keywords for the resulting collection
        :param BTC: the Bitcoin address of the resulting collection
    """
    bitmessage_connection = Bitmessage()
    address = bitmessage_connection.create_address(address_password)
    keywords = [Keyword(name=x) for x in keywords.split(",")]
    collection = Collection(
        title=title,
        description=description,
        address=address,
        accesses=0,
        votes=0,
        btc=btc,
        keywords=keywords,
        documents=[],
        creation_date=datetime.datetime.now(),
        oldest_date=datetime.datetime.now(),
        votes_last_checked=datetime.datetime.now(),
        latest_broadcast_date=datetime.datetime.now()
    )
    cache.insert_new_collection(collection)
    print ("Collection inserted with address/ID " + address)


def show_collection(collection_address):
    '''
    Displays information about a specific collection, including a document list
    :param collection_address: Collection address
    '''
    collection = cache.get_collection_with_address(collection_address)
    print ("\tID " + collection.address + "\t " + collection.title + \
           "\tCreation Date " + collection.creation_date.strftime("%A, %d. %B %Y %I:%M%p"))
    print ("\t" +"~~~~~~~~~~~~~~~"+ "Document list"+"~~~~~~~~~~~~~~~")
    print ("\t\t" + "URI" + "\t" + "Title" + "\t" + "Description")
    documents = cache.get_documents_from_collection(collection_address)
    for doc in documents:
        print ("\t\t" + doc.hash + "\t" + doc.title +  "\t" + doc.description)


def publish_collection(address_password, collection_address):
    bitmessage_connection = Bitmessage()
    address = bitmessage_connection.create_address(address_password)
    collection = cache.get_collection_with_address(collection_address)
    if collection is not None:
        collection_handler = Controller()
        collection_handler.publish_collection(collection, config.MAIN_CHANNEL_ADDRESS, address)
        print ("Collection published successfully!")
    else:
        print ("Collection not found in local cache.")
