## In this script, we will learn how to work with python from command line


## Introduction To Command Line Python

echo -e 'if __name__ == "__main__":\n    print("Welcome to a Python script")' > script.py
python script.py


## Using Different Python Versions

python3 script.py


## Installing Packages That Extend Python

pip install requests # will install the requests package


## Overview Of Virtual Environments

virtualenv python2


## Creating A Python 3 Virtualenv

virtualenv -p /usr/bin/python3 python3



## Activating A Virtualenv

source python3/bin/activate


## Verifying The Installed Packages

python -V # for current python version

pip freeze # for installed packages


## Importing Saved Functions Into A File

def print_message():
    print("Hello from another file!")

import utils

if __name__ == "__main__":
    utils.print_message()

python script.py
