import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

VERSION = '0.1.0'

config = {
    'description': 'Python Transition-Level Utilities',
    'long_description': read('README.md'),
    'author': 'Benjamin J. Morgan',
    'author_email': 'b.j.morgan@bath.ac.uk',
    'url': 'https://github.com/bjmorgan/tlpy',
    'download_url': "https://github.com/bjmorgan/tlpy/archive/%s.tar.gz" % (VERSION),
    'author_email': 'b.j.morgan@bath.ac.uk',
    'version': VERSION,
    'install_requires': [ 'numpy', 
                          'coverage',
                          'codeclimate-test-reporter' ],
    'license': 'MIT',
    'packages': ['tlpy'],
    'scripts': [],
    'name': 'tlpy'
}

setup(**config)
