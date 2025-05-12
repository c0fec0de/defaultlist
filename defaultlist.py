"""
Automatically Extending List.

Added indicies are filled with `None` by default.

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
"""

import sys


# pylint: disable=invalid-name
class defaultlist(list):

    """
    List extending automatically to the maximum requested length.

    Keyword Args:

        factory: Function called for every missing index.
    """

    def __init__(self, factory=None):
        self.__factory = factory or defaultlist.__nonefactory

    @staticmethod
    def __nonefactory():
        return None

    def __fill(self, index):
        missing = index - len(self) + 1
        if missing > 0:
            self += [self.__factory() for idx in range(missing)]

    def __setitem__(self, index, value):
        self.__fill(index)
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__getslice(index.start, index.stop, index.step)

        self.__fill(index)
        return list.__getitem__(self, index)

    def __getslice__(self, start, stop, step=None):  # pragma: no cover
        # python 2.x legacy
        if stop == sys.maxsize:
            stop = None
        return self.__getslice(start, stop, step)

    def __normidx(self, idx, default):
        if idx is None:
            idx = default
        elif idx < 0:
            idx += len(self)
        return idx

    def __getslice(self, start, stop, step):
        end = max((start or 0, stop-1 if stop else 0, 0))
        if end:
            self.__fill(end)
        start = self.__normidx(start, 0)
        stop = self.__normidx(stop, len(self))
        step = step or 1
        r = defaultlist(factory=self.__factory)
        for idx in range(start, stop, step):
            r.append(list.__getitem__(self, idx))
        return r

    def __add__(self, other):
        if isinstance(other, list):
            r = self.copy()
            r += other
            return r

        return list.__add__(self, other)

    def copy(self):
        """Return a shallow copy of the list. Equivalent to a[:]."""
        r = defaultlist(factory=self.__factory)
        r += self
        return r
