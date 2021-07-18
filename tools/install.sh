#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd -P )"
SCRIPT_FILE="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"

echo "run : $SCRIPT_FILE"
cd $SCRIPT_DIR

sudo apt-get update
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.6

echo "[select Python3.6]"
sudo update-alternatives --config python

sudo apt-get install -y wget net-tools zip curl vim git htop iftop
sudo apt-get install -y build-essential cmake
sudo apt-get install -y zlib1g-dev automake libtool autoconf git
sudo apt-get install -y subversion gawk flac
sudo apt-get install -y gfortran libblas-dev liblapack-dev
sudo apt-get install -y libatlas-dev libatlas-base-dev sox ffmpeg 
sudo apt-get install -y libatlas-base-dev liblapack-dev libblas-dev
sudo apt-get install -y openmpi-bin
sudo apt-get install -y libsndfile-dev swig
sudo apt-get install -y checkinstall libreadline-gplv2-dev libncursesw5-dev
sudo apt-get install -y libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev
sudo apt-get install -y openssl libffi-dev

sudo apt-get install -y python3.6-pip python3.6-dev python3.6-setuptools python3.6-venv python3.6-distutils python3.6-smbus python3.6-devel
sudo apt-get install -y python-pip python-dev
