Added indices are filled with `None` by default.

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

Simple factory functions can be created via `lambda`.

    >>> l = defaultlist(lambda: 'empty')
    >>> l[2] = "C"
    >>> l[4]
    'empty'
    >>> l
    ['empty', 'empty', 'C', 'empty', 'empty']

It is also possible to implement advanced factory functions:

    >>> def inc():
    ...     inc.counter += 1
    ...     return inc.counter
    >>> inc.counter = -1
    >>> l = defaultlist(inc)
    >>> l[2] = "C"
    >>> l
    [0, 1, 'C']
    >>> l[4]
    4
    >>> l
    [0, 1, 'C', 3, 4]

Please be aware that these functions are shared between shallow copies of the list.

    >>> c = l[1:-1]
    >>> c
    [1, 'C', 3]
    >>> c[5]
    7
    >>> c
    [1, 'C', 3, 5, 6, 7]
    >>> l[6]
    9
    >>> l
    [0, 1, 'C', 3, 4, 8, 9]
