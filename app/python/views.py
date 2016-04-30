from flask import render_template

from . import python

@python.route('/1-1')
def py1():
	return render_template('python/1-1.html')

@python.route('/1-2')
def py2():
	return render_template('python/1-2.html')