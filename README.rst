.. image:: https://badge.fury.io/py/defaultlist.svg
    :target: https://badge.fury.io/py/defaultlist

.. image:: https://travis-ci.org/c0fec0de/defaultlist.svg?branch=master
    :target: https://travis-ci.org/c0fec0de/defaultlist

.. image:: https://coveralls.io/repos/github/c0fec0de/defaultlist/badge.svg
    :target: https://coveralls.io/github/c0fec0de/defaultlist

.. image:: https://readthedocs.org/projects/defaultlist/badge/?version=0.1.0
    :target: http://defaultlist.readthedocs.io/en/0.1.0/?badge=0.1.0

.. image:: https://codeclimate.com/github/c0fec0de/defaultlist.png
    :target: https://codeclimate.com/github/c0fec0de/defaultlist

Documentation
=============

The Documentation_ is hosted on http://defaultlist.readthedocs.io/en/0.1.0/

.. _Documentation: http://defaultlist.readthedocs.io/en/0.1.0/

Getting started
===============

.. _getting_started:

List extending automatically to the maximum requested length.

Added indicies are filled with None by default.

>>> l = defaultlist()
>>> l
[]
>>> l[2] = "C"
>>> l
[None, None, 'C']
>>> l[4]
>>> l
[None, None, 'C', None, None]

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
