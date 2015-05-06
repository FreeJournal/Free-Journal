#!/usr/bin/python

import sys, datetime, uuid, shutil, os

# BitMessage installer imports
import platform
from bitmessage.install import apt_install, windows_install

# FreeNet installer imports
from freenet.install import linux_install

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

# Frontend imports
try:
    from frontend.webapp import app as webapp
except:
    print ("Error: could not import webapp.")

try:
    # Freenet may not be installed
    import freenet
    from freenet.FreenetConnection import FreenetConnection
    freenet_installed = True
except:
    freenet_installed = False

def print_help():
    """ Print usage instructions for the command-line library. """
    print ("Usage: ./freejournal [command]")
    print ("./freejournal_cli help [command name] - display extended command information.\n")
    print ("Available commands:")
    print ("\tgetdoc [document hash] [document output path/filename]")
    print ("\tputdoc [document input path] [collection address] [title] [description]")
    print ("\tlistcollections")
    print ("\tlistversions [collection address] [(optional) 'documents' to print document_ids]")
    print ("\tlisten")
    print ("\tinstall [freenet|bitmessage|all]")
    print ("\tshowcollection [index bitmessage ID]")
    print ("\tputcollection [address password] [title] [description] [keywords] ")
    print ("\tpublishcollection [address password] [index bitmessage ID]")
    print ("\twebapp")
    print ("\tuploader")
    print ("\tkeepalive")

def print_command_help(command):
    """ Display extended help information for CLI command
        :param command: FreeJournal command name"""
    COMMANDS = \
        { "getdoc": \
            "Get a document with given hash from the FreeJournal network storage.", \
          "putdoc": \
            "Add a document to the FreeJournal network storage and create the local" \
            + " corresponding document object, displaying the document ID required " \
            + " to retreive the document with the configured key.  To publish, " \
            + " call pubcollection with the returned document ID.", \
          "listcollections": \
            "List all document indexes currently known to this FreeJournal instance.", \
          "listversions": \
            "List all the versions of a particular collection", \
          "showcollection": \
            "Display all known details of a given collection, including all documents it indexes.", \
          "listen": \
            "Start the long-running FreeJournal listener.", \
          "install": \
            "Perform initial setup, installing FreeJournal dependencies.", \
          "putcollection": \
            "Create a new collection and store it locally.", \
          "publishcollection": \
            "Publish a local collection to the world (other FreeJournal nodes).", \
          "webapp": \
            "Run the FreeJournal web application (webapp).", \
          "uploader": \
            "Run the FreeJournal graphical desktop application/uploader.", \
          "keepalive": \
            "Run network keepalive functionality (republish indexes to the BitMessage network)." \
        }
    if command in COMMANDS:
        print (COMMANDS[command])
    else:
        print ("Unknown command!")
        print_help()

def get_doc_file(document_hash, document_output_filename):
    """ Get a document file from the Freenet network
        :param document_hash: the Freenet URI to retreive
        :param document_output_filename: path/filename to write to
    """
    freeCon = FreenetConnection()
    output=freeCon.get(document_hash)
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


def list_collection_version(collection_address, document_ids):
    versions = cache.get_versions_for_collection(collection_address)
    if(len(versions)!=0):
        print("Collection Versions for " + collection_address + ":" )
        print ("\t" + "Root hash" + "\t\t\t\t\t\t\t\t" + "Collection Version")
    else:
        print("Collection is empty")
    for version in versions:
        print("\t" + version.root_hash + "\t" + str(version.collection_version))
        if(document_ids == 'documents'):
            print("document_ids:")
            print(version.document_ids)
            print("")

def install_dependencies(dependency):
    """ Install a prerequisite (dependency) for deploying a FreeJournal
        node.  Rerun with each FreeJournal upgrade.
        :param dependency: Software to install, freenet/bitmessage/all
    """
    dependency = dependency.lower()
    if dependency == 'freenet' or dependency == 'all':
        os = sys.platform
        if 'linux' not in os:
            raise Exception("Invalid Operating System. See README.")
        else:
            linux_install()
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
    file_name = os.path.basename(file_path)
    contents = open(file_path).read()
    freeCon = FreenetConnection()
    uri = freeCon.put(contents)
    name, extension = os.path.splitext(file_name)
    hash_name = uri
    new_file_name = hash_name + extension
    shutil.copy(file_path, os.path.expanduser(config.DOCUMENT_DIRECTORY_PATH) + new_file_name)
    document = Document(
        collection_address = collection_address,
        description = description,
        hash = uri,
        title = title,
        filename = new_file_name,
        accesses = 0
    )
    cache.insert_new_document(document)
    collection = cache.get_collection_with_address(collection_address)
    collections.update_hash(collection)

def put_collection(address_password, title, description, keywords):
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
    cache = Cache()
    address = bitmessage_connection.create_address(address_password)

    input_keywords = [Keyword(name=x) for x in keywords.split(",")]
    keywords = []
    for key in input_keywords:
            db_key = cache.get_keyword_by_name(key.name)
            if db_key is not None:
                keywords.append(db_key)
            else:
                keywords.append(key)
    collection = Collection(
        title=title,
        description=description,
        address=address,
        accesses=0,
        votes=0,
        btc="btc",
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


def validate_cli_arguments(length):
    if (len(sys.argv) == length):
        return True
    print_help()

def process_command(command):
    """ Process a command-line command and execute the 
        resulting FreeJournal action
        :param command: The command to be executed, as a sys arg array
    """
    if len(sys.argv) < 2:
        print_help()
        return
    command = sys.argv[1].lower()
    if command == 'help':
        if (validate_cli_arguments(3)):
            print_command_help(sys.argv[2])
    elif command == 'getdoc':
        if (validate_cli_arguments(4)):
            get_doc_file(sys.argv[2], sys.argv[3])
    elif command == 'putdoc':
        if (validate_cli_arguments(6)):
            put_document(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    elif command == 'listcollections':
        list_collections()
    elif command == 'listversions':
        if (len(sys.argv) ==3):
            list_collection_version(sys.argv[2],None)
        elif (len(sys.argv)==4 and sys.argv[3]=='documents'):
            list_collection_version(sys.argv[2],sys.argv[3])    
        else:
            print_help()
    elif command == 'showcollection':
        if (validate_cli_arguments(3)):
            show_collection(sys.argv[2])
    elif command == 'listen':
        from bitmessage.bitmessage_listener import get_collections
        get_collections()
    elif command == 'install':
        if (validate_cli_arguments(3)):
            install_dependencies(sys.argv[2])
    elif command == 'putcollection':
        if (validate_cli_arguments(6)):
            put_collection(sys.argv[2], \
                sys.argv[3], sys.argv[4], \
                sys.argv[5])
    elif command == 'publishcollection':
        if (validate_cli_arguments(4)):
            publish_collection(sys.argv[2], sys.argv[3])
        else:
            print_help()
    elif command == 'webapp':
        webapp.run(debug = config.WEBAPP_DEBUG, port = config.WEBAPP_PORT)
    elif command == 'uploader':
        from frontend.uploader import fjUploaderGUI
        fjUploaderGUI.run()
    elif command == 'keepalive':
        from bitmessage.bitmessage_keepalive import find_old_collections
        find_old_collections(3)
    else:
        print_help()
