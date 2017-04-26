"""collections.defaultdict equivalent implementation of list."""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

config = {
    'name': "defaultlist",
    'version': "0.1.0",
    'author': 'c0fec0de',
    'author_email': 'c0fec0de@gmail.com',
    'description': " collections.defaultdict equivalent implementation of list.",
    'url': "https://github.com/c0fec0de/defaultlist",
    'license': 'Apache 2.0',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    'keywords': 'defaultlist list defaultdict collections',
    'py_modules': ['defaultlist'],
    'extras_require': {
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    'test_suite': 'nose.collector',
}

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    config['long_description'] = f.read()

setup(**config)
