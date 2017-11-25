.. image:: https://badge.fury.io/py/defaultlist.svg
    :target: https://badge.fury.io/py/defaultlist

.. image:: https://travis-ci.org/c0fec0de/defaultlist.svg?branch=master
    :target: https://travis-ci.org/c0fec0de/defaultlist

.. image:: https://coveralls.io/repos/github/c0fec0de/defaultlist/badge.svg
    :target: https://coveralls.io/github/c0fec0de/defaultlist

.. image:: https://readthedocs.org/projects/defaultlist/badge/?version=1.0.0
    :target: http://defaultlist.readthedocs.io/en/1.0.0/?badge=1.0.0

.. image:: https://codeclimate.com/github/c0fec0de/defaultlist.png
    :target: https://codeclimate.com/github/c0fec0de/defaultlist

.. image:: https://img.shields.io/pypi/pyversions/defaultlist.svg
   :target: https://pypi.python.org/pypi/defaultlist

.. image:: https://landscape.io/github/c0fec0de/defaultlist/master/landscape.svg?style=flat
   :target: https://landscape.io/github/c0fec0de/defaultlist/master

Documentation
=============

The Documentation_ is hosted on http://defaultlist.readthedocs.io/en/1.0.0/

.. _Documentation: http://defaultlist.readthedocs.io/en/1.0.0/

Getting started
===============

.. _getting_started:

List extending automatically to the maximum requested length.

Added indicies are filled with None by default.

>>> from defaultlist import defaultlist
>>> l = defaultlist()
>>> l
[]
>>> l[2] = "C"
>>> l
[None, None, 'C']
>>> l[4]
>>> l
[None, None, 'C', None, None]

Slices and negative indicies are supported likewise

>>> l[1:4]
[None, 'C', None]
>>> l[-3]
'C'

Simple factory functions can be created via lambda.

>>> l = defaultlist(lambda: 'empty')
>>> l[2] = "C"
>>> l[4]
'empty'
>>> l
['empty', 'empty', 'C', 'empty', 'empty']

Installation
============

To install the `defaultlist` module run::

    pip install defaultlist

If you do not have write-permissions to the python installation, try::

    pip install defaultlist --user
