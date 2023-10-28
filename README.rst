.. image:: https://badge.fury.io/py/defaultlist.svg
    :target: https://badge.fury.io/py/defaultlist

.. image:: https://img.shields.io/pypi/dm/defaultlist.svg?label=pypi%20downloads
   :target: https://pypi.python.org/pypi/defaultlist

.. image:: https://readthedocs.org/projects/defaultlist/badge/?version=latest
    :target: https://defaultlist.readthedocs.io/en/latest/?badge=latest

.. image:: https://coveralls.io/repos/github/c0fec0de/defaultlist/badge.svg
    :target: https://coveralls.io/github/c0fec0de/defaultlist

.. image:: https://readthedocs.org/projects/defaultlist/badge/?version=1.0.0
    :target: https://defaultlist.readthedocs.io/en/1.0.0/?badge=1.0.0

.. image:: https://img.shields.io/pypi/pyversions/defaultlist.svg
   :target: https://pypi.python.org/pypi/defaultlist

.. image:: https://img.shields.io/badge/code%20style-pep8-brightgreen.svg
   :target: https://www.python.org/dev/peps/pep-0008/

.. image:: https://img.shields.io/badge/code%20style-pep257-brightgreen.svg
   :target: https://www.python.org/dev/peps/pep-0257/

.. image:: https://img.shields.io/badge/linter-pylint-%231674b1?style=flat
   :target: https://www.pylint.org/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/github/contributors/c0fec0de/defaultlist.svg
   :target: https://github.com/c0fec0de/defaultlist/graphs/contributors/

.. image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
   :target: http://makeapullrequest.com

.. image:: https://img.shields.io/github/issues-pr/c0fec0de/defaultlist.svg
   :target: https://github.com/c0fec0de/defaultlist/pulls

.. image:: https://img.shields.io/github/issues-pr-closed/c0fec0de/defaultlist.svg
   :target: https://github.com/c0fec0de/defaultlist/pulls?q=is%3Apr+is%3Aclosed


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
