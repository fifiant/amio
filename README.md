amio
====

Easy way to build your own developement environment

Prerequisites
=============

	:: Linux
	$ sudo apt-get install virtualbox rubygems

	:: Mac OS X
	$ brew install 

	or install dmg here : https://www.virtualbox.org/wiki/Downloads

Installation
============

	$ python bootstrap.py
	$ bin/buildout

Start the machine
==================

	$ vagrant up

Setup the machine
=================

	$ bin/fab vagrant install

Run the machine
===============
	$ ip_adresse:3000