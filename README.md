# Free-Journal

Project Homepage: http://freejournal.org/
Example Node: http://freejournal.io/

## Prerequisites

The first step to installing FreeJournal is to ensure you have:
- A Linux-based operating systems (for security reasons, we do not support Windows)
- Python 2.x
- python-pip (the pip command)
- [PyBitmessage](https://github.com/Bitmessage/PyBitmessage/) (install script provided)
- [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib)
- [FreeNet](https://freenetproject.org) (install script provided)

If you are on Windows, you can still browse one of many existing FreeJournal nodes.
Consult a list on our website.

Run python install.py in bitmessage/ and in freenet/
to install the required prerequisites, then modify config.py to 
change your local node settings.

To install database, documentation, and other library requirements, run
``pip install -r requirements.txt`` on the root directory.

## Generating Documentation

To generate API documentation, simply `sh generate_docs.sh` and check the `docs` folder
for output.

## Running FreeJournal

Coming soon

## Running FreeJournal Unit Tests

Simply `python run_tests.py` in the root directory after installing the required
prerequisites.
