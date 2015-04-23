from .config import RUN_PYBITMESSAGE_LINUX
import subprocess
import os
import shutil


def check_config_creation():
    """
    Checks whether PyBitmessage has created its keys.dat file
    Linux specific for now, but will be modified for other operating systems
    """
    return os.path.exists(os.path.expanduser("~/.config/PyBitmessage/keys.dat"))


def apt_install():
    """
    Generic installation for linux versions using apt
    """
    subprocess.call(["sudo apt-get update"], shell=True)
    subprocess.call(
        ["sudo apt-get install openssl git python-qt4"], shell=True)

    try:
        subprocess.call(
            ["git clone https://github.com/Bitmessage/PyBitmessage $HOME/PyBitmessage"], shell=True)
    except:
        print (
            'PyBitmessage already installed or we received a permission denied error')

    devnull = open(os.devnull, 'wb')
                   # Used to ignore the enormous amount of output from
                   # PyBitmessage

    # Run Pybitmessage so it can create the keys.dat file
    process = subprocess.Popen(
        ["exec " + RUN_PYBITMESSAGE_LINUX], shell=True, stdout=devnull, stderr=devnull)

    # Wait until PyBitmessage creates the appropriate .config file structure
    while not check_config_creation():
        pass

    process.kill()

    # Copy our modified keys.dat file to the user's ~/.config/PyBitmessage
    shutil.copyfile(os.path.abspath(os.path.join(os.path.dirname(__file__))) +
                    "/installfiles/keys.dat", os.path.expanduser("~/.config/PyBitmessage/keys.dat"))


def windows_install():
    """
    Error message 
    """
    print ('FATAL ERROR: We detected you are using an inferior operating system to Linux...')
