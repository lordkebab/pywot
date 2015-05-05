from distutils.core import setup

setup(
	name='pywot', 
	packages=['pywot'], 
	version='1.0', 
	description='A python interface to Wargaming.net\'s World of Tanks API', 
	install_requires=[
		'requests'
	],
	author='Matt Selph', 
	author_email='matt.selph@gmail.com', 
	url='https://github.com/mattselph/pywot', 
	download_url='https://github.com/mattselph/pywot/tarball/v0.1',
	keywords=['world of tanks', 'wargaming', 'wot'],
	classifiers=[]
)
