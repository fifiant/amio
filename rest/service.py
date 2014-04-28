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


from flask import Flask, render_template, request, redirect, url_for, flash
import yaml

# App config.
SECRET_KEY = '87469976308fd14a2d0148247d441f2756b6176a'
app = Flask(__name__)
	
@app.route('/')
def index():
	"""Render website's home page."""
	return render_template('home.html')

@app.route('/about/')
def about():
	 """Render the website's about page."""
	 return render_template('about.html')

@app.route('/template')
def template():
	""" Render the website's Vagrant templates."""
	return render_template('template.html')

@app.route('/generate', methods=['POST'])
def generate():
	""" """
	error = None
	error1 = None
	data = {}
	if request.method == 'POST':
		form = request.form['form']
		print "Form == %s"  % form
		if form == "form1":
			name = request.form['name']
			hostname = request.form['hostname']
			ipadress = request.form['ipadress']
			macadress = request.form['macadress']
			memory = request.form['memory']
			cpu = request.form['cpu']
			instance = request.form['instance']
			if name is None or name =="":
				error = 'You have to enter a machine name'
			elif hostname is None or hostname=="":
				error = 'You have to enter a hostname'
				print "Error : %s" % error
			elif ipadress is None or ipadress=="":
				error = 'You have to enter a ipadress'
			elif macadress is None or macadress =="":
				error = 'You have to enter a macadress'
			elif memory is None or memory == "":
				error = 'You have to enter a memory size'
			elif cpu is None or cpu =="":
				error = 'You have to enter a cpu'
			elif instance is None or instance =="":
				error = 'You have to enter a instance number'
			else:
				data['name'] = name
				data['hostname'] = hostname
				data['ipadress'] = ipadress
				data['macadress'] = macadress
				data['memory'] = memory
				data['cpu'] = cpu
				data['instance'] = instance
				# Generate config
				generateConfig(instance, data)
				return redirect(url_for('template'))
				#return render_template('template.html', error=error)
		if request.form['form'] == "form2":
			pass
		if error != None:
			return render_template('template.html', error=error)
		if error1 != None :
			return render_template('template.html', error=error1)
	else:
		print "Bad request == %s" % request.method
	return render_template('template.html', error=error1)

@app.route('/manage')
def manage():
	return "0"

@app.errorhandler(404)
def page_not_found(error):
	 """Custom 404 page."""
	 return render_template('404.html'), 404
# Utils 
def generateConfig(instance, data):
	with open('config.yml', 'w') as outfile:
		outfile.write( yaml.dump(data, default_flow_style=False) )
if __name__ == '__main__':
	app.run(debug=True) # rune the application
