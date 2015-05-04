import subprocess
import os
import sys


def linux_install():
    """
    This is the installation script for *nix based systems
    Requires: java
    """
    try:
        subprocess.call(
            ["wget 'https://freenetproject.org/jnlp/freenet_installer.jar' -O new_installer_offline.jar"], shell=True)
        subprocess.call(["java -jar new_installer_offline.jar"], shell=True)
        i = 43
    except:
        print('Java not installed, or wget failed')
