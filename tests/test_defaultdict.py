from defaultlist import defaultlist
from nose.tools import eq_

from helper import assert_raises


def test_simple():
    """Simple scenario."""
    l = defaultlist()
    eq_(l, [])
    l[2] = "C"
    eq_(l, [None, None, 'C'])
    l[4]
    eq_(l, [None, None, 'C', None, None])


def test_inc():
    """Count the number of func invocations."""
    def inc():
        inc.counter += 1
        return inc.counter
    inc.counter = -1

    l = defaultlist(inc)
    eq_(l, [])
    l[2] = "C"
    eq_(l, [0, 1, 'C'])
    eq_(l[4], 4)
    eq_(l, [0, 1, 'C', 3, 4])
    eq_(l[1], 1)
    eq_(l, [0, 1, 'C', 3, 4])


def test_op():
    """default operations."""
    l = defaultlist()
    l[2] = "C"
    l[4]
    eq_(l, [None, None, 'C', None, None])
    l.insert(3, 'D')
    eq_(l, [None, None, 'C', 'D', None, None])
    l.remove(None)
    eq_(l, [None, 'C', 'D', None, None])


def test_add():
    a = defaultlist()
    b = [1, 2]
    a_a = a + a
    eq_(a_a, [])
    a_b = a + b
    eq_(a_b, [1, 2])
    a_b[5] = 7
    eq_(a, [])
    eq_(b, [1, 2])
    eq_(a_b, [1, 2, None, None, None, 7])
    with assert_raises(TypeError, 'can only concatenate list (not "int") to list'):
        a + 4


def test_iadd():
    """iadd operator."""
    a = defaultlist()
    b = [1, 2]
    a += a
    eq_(a, [])
    a += b
    eq_(a, [1, 2])
    a[5] = 7
    eq_(b, [1, 2])
    eq_(a, [1, 2, None, None, None, 7])
    with assert_raises(TypeError, "'int' object is not iterable"):
        a += 4


def test_slice():
    """Slice selection."""
    l = defaultlist()
    l += list(range(5))
    eq_(l, [0, 1, 2, 3, 4])
    c = l[1:]
    eq_(c, [1, 2, 3, 4])
    c = l[1:-1]
    eq_(c, [1, 2, 3])
    c[5] = 'c0fe'
    eq_(c, [1, 2, 3, None, None, 'c0fe'])


def test_slice_ref():
    """Slice reference implementation."""
    r = list(range(10))
    l = defaultlist()
    l += r
    eq_(l[-4:9], r[-4:9])
    eq_(l[0:9], r[0:9])
    eq_(l[:9], r[:9])
    eq_(l[-4:8], r[-4:8])
    eq_(l[0:], r[0:])
    eq_(l[:-2], r[:-2])
    eq_(list(l), r)


def test_slice_step():
    """Slice Selection with step."""
    l = defaultlist()
    l[0] = 'a'
    l[1] = 'b'
    l[2] = 'c'
    l[3] = 'd'
    l[4] = 'e'
    l[5] = 'f'

    d = l[1:6:2]
    eq_(l, ['a', 'b', 'c', 'd', 'e', 'f', None])
    eq_(d, ['b', 'd', 'f'])

    d = l[:6:2]
    eq_(l, ['a', 'b', 'c', 'd', 'e', 'f', None])
    eq_(d, ['a', 'c', 'e'])

    d = l[1:6:2]
    eq_(l, ['a', 'b', 'c', 'd', 'e', 'f', None])
    eq_(d, ['b', 'd', 'f'])

    d = l[:7:2]
    eq_(l, ['a', 'b', 'c', 'd', 'e', 'f', None, None])
    eq_(d, ['a', 'c', 'e', None])

    d = l[1:7:2]
    eq_(l, ['a', 'b', 'c', 'd', 'e', 'f', None, None])
    eq_(d, ['b', 'd', 'f'])

    d = l[::2]
    eq_(l, ['a', 'b', 'c', 'd', 'e', 'f', None, None])
    eq_(d, ['a', 'c', 'e', None])

    d = l[1::2]
    eq_(l, ['a', 'b', 'c', 'd', 'e', 'f', None, None])
    eq_(d, ['b', 'd', 'f', None])

    d = l[1::]
    eq_(l, ['a', 'b', 'c', 'd', 'e', 'f', None, None])
    eq_(d, ['b', 'c', 'd', 'e', 'f', None, None])


def test_copy():
    """copy()."""
    l = defaultlist()
    l[2] = "C"
    l[4]
    eq_(l, [None, None, 'C', None, None])
    c = l.copy()
    eq_(c, [None, None, 'C', None, None])
    assert isinstance(c, defaultlist)
    c[6] = 'c0fe'
    eq_(c, [None, None, 'C', None, None, None, 'c0fe'])


def test_copy_inc():
    """copy() using inc."""
    def inc():
        inc.counter += 1
        return inc.counter
    inc.counter = -1
    l = defaultlist(inc)
    l[2] = "C"
    l[4]
    eq_(l, [0, 1, 'C', 3, 4])
    c = l.copy()
    eq_(c, [0, 1, 'C', 3, 4])
    assert isinstance(c, defaultlist)
    c[6] = 'c0fe'
    eq_(c, [0, 1, 'C', 3, 4, 5, 'c0fe'])
    l[6]
    eq_(l, [0, 1, 'C', 3, 4, 7, 8])


def test_len():
    """Length."""
    l = defaultlist()
    eq_(len(l), 0)
    l[2] = "C"
    eq_(len(l), 3)
    l[4]
    eq_(len(l), 5)

def test_initial_data():
    l = defaultlist(None, ['a', 'b'])
    eq_(len(l), 2)
    l[15] = 42
    eq_(len(l), 16)
    eq_(l[1], 'b')

    l2 = defaultlist(None, [None, None, 1, None])
    eq_(len(l2), 4)
    l2[1] = 'q'
    eq_(l2[1:3], ['q', 1])
    eq_(l2[-1], None)
    l2[-1] = 'last?'
    eq_(l2[-1], 'last?')
