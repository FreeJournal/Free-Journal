import subprocess


def rabbitmq_install():
    """
    Generic installation for linux versions using apt
    """
    subprocess.call(["sudo apt-get update"], shell=True)
    subprocess.call(["sudo apt-get install rabbitmq -y"], shell=True)
