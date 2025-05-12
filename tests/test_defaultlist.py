"""Basic Testing."""
from pytest import raises

from defaultlist import defaultlist

# pylint: disable=use-implicit-booleaness-not-comparison


def test_simple():
    """Simple scenario."""
    dfl = defaultlist()
    assert dfl == []
    dfl[2] = "C"
    assert dfl == [None, None, "C"]
    assert dfl[4] is None
    assert dfl == [None, None, "C", None, None]


def test_inc():
    """Count the number of func invocations."""

    def inc():
        inc.counter += 1
        return inc.counter

    inc.counter = -1

    dfl = defaultlist(inc)
    dfl[2] = "C"
    assert dfl == [0, 1, "C"]
    assert dfl[4] == 4
    assert dfl == [0, 1, "C", 3, 4]
    assert dfl[1] == 1
    assert dfl == [0, 1, "C", 3, 4]


def test_op():
    """default operations."""
    dfl = defaultlist()
    dfl[2] = "C"
    assert dfl[4] is None
    assert dfl == [None, None, "C", None, None]
    dfl.insert(3, "D")
    assert dfl == [None, None, "C", "D", None, None]
    dfl.remove(None)
    assert dfl == [None, "C", "D", None, None]


def test_add():
    """Add Operation."""
    a = defaultlist()
    b = [1, 2]
    a_a = a + a
    assert a_a == []
    a_b = a + b
    assert a_b == [1, 2]
    a_b[5] = 7
    assert a == []
    assert b == [1, 2]
    assert a_b == [1, 2, None, None, None, 7]
    with raises(TypeError):
        a = a + 4


def test_iadd():
    """iadd operator."""
    a = defaultlist()
    b = [1, 2]
    a += a
    assert a == []
    a += b
    assert a == [1, 2]
    a[5] = 7
    assert b == [1, 2]
    assert a == [1, 2, None, None, None, 7]
    with raises(TypeError):
        a += 4


def test_slice():
    """Slice selection."""
    dfl = defaultlist()
    dfl += list(range(5))
    assert dfl == [0, 1, 2, 3, 4]
    c = dfl[1:]
    assert c == [1, 2, 3, 4]
    c = dfl[1:-1]
    assert c == [1, 2, 3]
    c[5] = "c0fe"
    assert c == [1, 2, 3, None, None, "c0fe"]


def test_slice_ref():
    """Slice reference implementation."""
    rng = list(range(10))
    dfl = defaultlist()
    dfl += rng
    assert dfl[-4:9] == rng[-4:9]
    assert dfl[0:9] == rng[0:9]
    assert dfl[:9] == rng[:9]
    assert dfl[-4:8] == rng[-4:8]
    assert dfl[0:] == rng[0:]
    assert dfl[:-2] == rng[:-2]
    assert dfl[:10] == rng[:10]
    assert list(dfl) == rng


def test_slice_step():
    """Slice Selection with step."""
    dfl = defaultlist()
    dfl[0] = "a"
    dfl[1] = "b"
    dfl[2] = "c"
    dfl[3] = "d"
    dfl[4] = "e"
    dfl[5] = "f"

    dat = dfl[1:6:2]
    assert dfl == ["a", "b", "c", "d", "e", "f"]
    assert dat == ["b", "d", "f"]

    dat = dfl[:6:2]
    assert dfl == ["a", "b", "c", "d", "e", "f"]
    assert dat == ["a", "c", "e"]

    dat = dfl[1:6:2]
    assert dfl == ["a", "b", "c", "d", "e", "f"]
    assert dat == ["b", "d", "f"]

    dat = dfl[:7:2]
    assert dfl == ["a", "b", "c", "d", "e", "f", None]
    assert dat == ["a", "c", "e", None]

    dat = dfl[1:7:2]
    assert dfl == ["a", "b", "c", "d", "e", "f", None]
    assert dat == ["b", "d", "f"]

    dat = dfl[::2]
    assert dfl == ["a", "b", "c", "d", "e", "f", None]
    assert dat == ["a", "c", "e", None]

    dat = dfl[1::2]
    assert dfl == ["a", "b", "c", "d", "e", "f", None]
    assert dat == ["b", "d", "f"]

    dat = dfl[1::]
    assert dfl == ["a", "b", "c", "d", "e", "f", None]
    assert dat == ["b", "c", "d", "e", "f", None]


def test_copy():
    """copy()."""
    dfl = defaultlist()
    dfl[2] = "C"
    assert dfl[4] is None
    assert dfl == [None, None, "C", None, None]
    cpy = dfl.copy()
    assert cpy == [None, None, "C", None, None]
    assert isinstance(cpy, defaultlist)
    cpy[6] = "c0fe"
    assert cpy == [None, None, "C", None, None, None, "c0fe"]


def test_copy_inc():
    """copy() using inc."""

    def inc():
        inc.counter += 1
        return inc.counter

    inc.counter = -1
    dfl = defaultlist(inc)
    dfl[2] = "C"
    assert dfl[4] == 4
    assert dfl == [0, 1, "C", 3, 4]
    cpy = dfl.copy()
    assert cpy == [0, 1, "C", 3, 4]
    assert isinstance(cpy, defaultlist)
    cpy[6] = "c0fe"
    assert cpy == [0, 1, "C", 3, 4, 5, "c0fe"]
    assert dfl[6] == 8
    assert dfl == [0, 1, "C", 3, 4, 7, 8]


def test_len():
    """Length."""
    dfl = defaultlist()
    assert len(dfl) == 0
    dfl[2] = "C"
    assert len(dfl) == 3
    assert dfl[4] is None
    assert len(dfl) == 5
