# -*- coding: utf-8 -*-
'''
AMIO ::: DevEnv
---------------

This module provides user developement environment using REST. 

:copyright: (c) 2014 by Fawaz PARAISO.
:license: Apache 2, see LICENSE for more details.
'''

__version_info__ = ('0', '2', '10')
__version__ = '.'.join(__version_info__)
__author__ = 'Fawaz PARAISO'
__license__ = 'Apache 2'
__copyright__ = '(c) 2014 by Fawaz PARAISO'
__all__ = ['AMIO']


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
	
@app.route('/')
def index():
	"""Render website's home page."""
	return render_template('home.html')

@app.route('/about/')
def about():
	 """Render the website's about page."""
	 return render_template('about.html')


@app.route('/manage')
def manage():
	return "0"

@app.errorhandler(404)
def page_not_found(error):
	 """Custom 404 page."""
	 return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True) # rune the application
