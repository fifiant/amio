#!/bin/bash

// Alternative option
// wget https://bitbucket.org/pypa/setuptools/raw/0.8/ez_setup.py
// sudo /usr/bin/python ez_setup.py

// To fix Mac OS X Bug
sudo pip install -U distribute

// To fix pyCrpto installation on Mac Os X (https://bugs.launchpad.net/pycrypto/+bug/1292408) ToDo
sudo CFLAGS=-Wunused-command-line-argument-hard-error-in-future pip install -U pycrypto