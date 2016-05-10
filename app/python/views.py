from flask import render_template

from . import python

@python.route('/1-1')
def py1():
	return render_template('python/1-1.html')

@python.route('/1-2')
def py2():
	return render_template('python/1-2.html')

@python.route('/1-3')
def py3():
	return render_template('python/1-3.html')

@python.route('/1-4')
def py4():
	return render_template('python/1-4.html')











@python.route('/sz1')
def sz1():
	return render_template('python/sz1.html')


@python.route('/ym1')
def ym1():
	return render_template('python/ym1.html')