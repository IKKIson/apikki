#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd -P )"
SCRIPT_FILE="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"

echo "run : $SCRIPT_FILE"
cd $SCRIPT_DIR

cd $SCRIPT_DIR/tools
./install.sh

cd $SCRIPT_DIR
python3.6 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip3 install --upgrade pip3

cd $SCRIPT_DIR/tools
./install_requirements.sh
