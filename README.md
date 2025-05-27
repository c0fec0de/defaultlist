[![PyPI Version](https://badge.fury.io/py/defaultlist.svg)](https://badge.fury.io/py/defaultlist)
[![Python Build](https://github.com/c0fec0de/defaultlist/actions/workflows/main.yml/badge.svg)](https://github.com/c0fec0de/defaultlist/actions/workflows/main.yml)
[![Documentation](https://readthedocs.org/projects/defaultlist/badge/?version=stable)](https://defaultlist.readthedocs.io/en/stable/?badge=stable)
[![Coverage Status](https://coveralls.io/repos/github/c0fec0de/defaultlist/badge.svg?branch=main)](https://coveralls.io/github/c0fec0de/defaultlist?branch=main)
[![python-versions](https://img.shields.io/pypi/pyversions/defaultlist.svg)](https://pypi.python.org/pypi/defaultlist)
[![contributors](https://img.shields.io/github/contributors/c0fec0de/defaultlist.svg)](https://github.com/c0fec0de/defaultlist/graphs/contributors/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Pull Requests](https://img.shields.io/github/issues-pr/c0fec0de/defaultlist.svg)](https://github.com/c0fec0de/defaultlist/pulls)
[![Pull Requests Closed](https://img.shields.io/github/issues-pr-closed/c0fec0de/defaultlist.svg)](https://github.com/c0fec0de/defaultlist/pulls?q=is%3Apr+is%3Aclosed)


# Automatically Extending List

* [Documentation](https://defaultlist.readthedocs.io/en/stable/)
* [PyPI](https://pypi.org/project/defaultlist/)
* [Sources](https://github.com/c0fec0de/defaultlist)
* [Issues](https://github.com/c0fec0de/defaultlist/issues)

## Getting started

List extending automatically to the maximum requested length.

Added indices are filled with None by default.

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

Slices and negative indices are supported likewise

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

## Installation

Installing it is pretty easy:

```bash
pip install defaultlist
```
