# MIT License
#
# Copyright (c) 2025 c0fec0de
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Automatically Extending List.
"""

import sys


class defaultlist(list):  # noqa: N801
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
        end = max((start or 0, stop - 1 if stop else 0, 0))
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
