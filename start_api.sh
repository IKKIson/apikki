#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd -P )"
SCRIPT_FILE="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"

echo "run : $SCRIPT_FILE"
cd $SCRIPT_DIR

# python3 app/main.py
nohup python3 app/main.py &
