#!/bin/bash

# Check for Python 3
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is required to install Joker-Eye Network Scanner."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check for pip
if ! command -v pip &>/dev/null; then
    echo "pip is required to install dependencies."
    echo "Please install pip and try again."
    exit 1
fi

# Install dependencies
pip install -r requirements.txt

# Install Joker-Eye Network Scanner
python3 setup.py install

echo "Joker-Eye Network Scanner is now installed."
echo "You can run it using 'joker-eye' command."

exit 0
