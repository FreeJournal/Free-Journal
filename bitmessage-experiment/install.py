from config.config import *
import subprocess
import sys
import os
import shutil


def check_config_creation():
    """Checks whether PyBitmessage has created its keys.dat file

    Linux specific for now, but will be modified for other operating systems
    """

    return os.path.exists(os.path.expanduser("~/.config/PyBitmessage/keys.dat"))


def linux_install():
    """Generic installation for linux operating systems

    Currently requires sudo to be installed
    Needs more testing
    """

    subprocess.call(["sudo apt-get install openssl git python-qt4"], shell=True)

    try:
        subprocess.call(["git clone https://github.com/Bitmessage/PyBitmessage $HOME/PyBitmessage"], shell=True)
    except:
        print 'PyBitmessage already installed or we received a permission denied error'

    devnull = open(os.devnull, 'wb')  # Used to ignore the enormous amount of output from PyBitmessage

    # Run Pybitmessage so it can create the keys.dat file
    process = subprocess.Popen(["exec " + RUN_PYBITMESSAGE], shell=True, stdout=devnull, stderr=devnull)

    # Wait until PyBitmessage creates the appropriate .config file structure
    while not check_config_creation():
        pass

    process.kill()

    # Copy our modified keys.dat file to the user's ~/.config/PyBitmessage
    shutil.copyfile("./config/keys.dat", os.path.expanduser("~/.config/PyBitmessage/keys.dat"))


def windows_install():
    print 'FATAL ERROR: We detected you are using an inferior operating system to Linux...'

if __name__ == '__main__':
    os_version = sys.platform
    if 'linux' in os_version:
        linux_install()
        print 'Installation Completed'
    elif 'windows' in os_version:
        windows_install()
    else:
        print "Couldn't detect a valid operating system"