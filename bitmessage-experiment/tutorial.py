import xmlrpclib
import time
import subprocess
import os
import sys
from config.config import *
from bitmessage_file import BitMessageFile
import base64


def launch_bitmessage():
    """Used to start up the PyBitmessage client so that we can connect to the api
    """

    os_version = sys.platform
    print 'Running BitMessage Tutorial on ' + os_version

    if 'linux' in os_version:

        devnull = open(os.devnull, 'wb')  # Used to ignore the ENORMOUS amount of output from PyBitmessage

        subprocess.Popen([RUN_PYBITMESSAGE], shell=True, stdout=devnull, stderr=devnull)  # Start up PyBitmessage


def api_connect():
    """Connect to the Bitmessage client
    """
    return xmlrpclib.ServerProxy(BITMESSAGE_SERVER)


def api_broadcast(from_address, subject, message):
    """Sends a broadcast to subscribers
    :param from_address: a valid address for bitmessage
    :param subject: base64 encoded text
    :param message: base64 encoded text
    """
    ack_data = api.sendBroadcast(from_address, subject, message)

    print 'Sending Broadcast...'

    status = ''
    while 'sent' not in status:
        status = api.getStatus(ack_data)
        print status
        time.sleep(5)


if __name__ == '__main__':
    args = sys.argv

    if len(args) != 2:
        print 'Please pass a path to a file'

    #Try connecting via the api first to see if PyBitmessage is already running
    try:
        api = api_connect()
        assert(5 == api.add(2, 3))
    except:
        launch_bitmessage()
        api = api_connect()

    print 'Waiting for connection'

    #Wait for api to connect to the bitmessage client
    connected = False
    while not connected:
        try:
            assert(5 == api.add(2, 3))
            connected = True
        except:
            pass

    print 'Connected successfully'

    # Create a basic file class
    bitmessage_file = BitMessageFile(args[1])

    file_hash = bitmessage_file.get_hash()
    file_name = bitmessage_file.get_file_name()

    # Construct a new address (testing purposes) and broadcast a test message
    address_label = base64.b64encode(file_name)
    broadcast_address = api.createRandomAddress(address_label)
    broadcast_subject = base64.b64encode("~Test~")
    broadcast_message = base64.b64encode(file_hash)

    api_broadcast(broadcast_address, broadcast_subject, broadcast_message)
