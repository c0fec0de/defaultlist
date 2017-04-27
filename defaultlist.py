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


class defaultlist(list):

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
        assert isinstance(index, int), "Invalid index: %r of %r" % (index, type(index))
        assert index >= 0, "Invalid index: %r" % index
        missing = index - len(self) + 1
        if missing > 0:
            try:
                for idx in range(missing):
                    self.append(self.__factory())
            except OverflowError:
                assert False, "Foo %r" % (missing)

    def __setitem__(self, index, value):
        self.__fill(index)
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__getslice(index.start, index.stop, index.step)
        else:
            self.__fill(index)
            return list.__getitem__(self, index)

    def __getslice__(self, start, stop, step=None):  # pragma: no cover
        # python 2.x legacy
        return self.__getslice(start, stop, step)

    def __getslice(self, start, stop, step):
            start = start or 0
            step = step or 1
            if stop is None:
                stop = len(self)
            elif stop < 0:
                stop = len(self) + stop
            else:
                self.__fill(stop)
                stop += 1
            assert len(self) >= stop
            r = defaultlist(factory=self.__factory)
            print("FOO", start, stop, step, list(range(start, stop, step)), self)
            for idx in range(start, stop, step):
                r.append(list.__getitem__(self, idx))
            return r

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
