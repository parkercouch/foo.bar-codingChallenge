try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
    'description': 'Google coding challenge',
    'author': 'Parker Couch',
    'url': 'none',
    'download_url': 'none',
    'author_email': 'parkercouch@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['coding_challenge'],
    'scripts': [],
    'name': 'coding_challenge'
}

setup(**config)