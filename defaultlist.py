"""
List extending automatically to the maximum requested length.

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

if hasattr(list, "__getslice__"):  # pragma: no cover
    def _getslice(self, start, end):
        r = defaultlist(factory=self.__factory)
        r += list.__getslice__(self, start, end)
        return r
else:
    _getslice = None


class defaultlist(list):

    __getslice__ = _getslice

    def __init__(self, factory=None):
        """
        List extending automatically to the maximum requested length.

        Keyword Args:

            factory: Function called for every missing index.
        """
        if factory is None:
            def factory():
                return None
        self.__factory = factory

    def __fill(self, index):
        missing = index - len(self) + 1
        if missing > 0:
            self += [self.__factory() for _ in range(missing)]

    def __setitem__(self, index, value):
        self.__fill(index)
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        if isinstance(index, slice):
            self.__fill(index.stop)
            r = defaultlist(factory=self.__factory)
            r += list.__getitem__(self, index)
            return r
        else:
            self.__fill(index)
            return list.__getitem__(self, index)

    def __add__(self, other):
        if isinstance(other, list):
            r = self.copy()
            r += other
            return r
        else:
            return list.__add__(self, other)

    def copy(self):
        """Return a shallow copy of the list. Equivalent to a[:]."""
        r = defaultlist(factory=self.__factory)
        r += self
        return r
