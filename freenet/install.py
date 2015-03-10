import subprocess, sys, os, shutil
'''
This is the installation script for *nix based systems 
Requires: java
'''
def linux_install():
    
    try:
        subprocess.call(["wget 'https://freenetproject.org/jnlp/freenet_installer.jar' -O new_installer_offline.jar"], shell=True)
        subprocess.call(["java -jar new_installer_offline.jar"], shell=True)
        i=43
    except:
        print('Java not installed, or wget failed')

if __name__ == '__main__':
    os = sys.platform
    if 'linux' not in os:
        raise Error("Invalid Operating System. lrn2penguin")    
    else:
        linux_install()
