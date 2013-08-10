from util import validate
import py

@validate(a=int, b=str, c=float, d=dict, e=list)
def fn(a, b, c, d, e):
    i = a + 1
    return (a, b, c, d, e)

@validate(b=int, d=dict)
def fn2(a, b, c, d):
    return (a, b, c, d)


def test_all():
    assert fn(1, '123', 1.0, {'a':1}, [2]) == (1, '123', 1.0, {'a':1}, [2]) 


def test_missing_args():
    py.test.raises(TypeError, "fn(1, '123', 1.0)")


def test_int():
    py.test.raises(TypeError, "fn(1.0, '123', 1.0, {'a', 2}, [1])")


def test_float():
    py.test.raises(TypeError, "fn(1, '123', '1', {'a', 2}, [1])")


def test_string():
    py.test.raises(TypeError, "fn(1, 123, '1', {'a', 2}, [1])")


def test_list():
    py.test.raises(TypeError, "fn(1, 123, '1', {'a', 2}, '1')")


def test_dict():
    py.test.raises(TypeError, "fn(1, 123, '1', 2, [1])")


def test_partial_spec():
    assert fn2(1.0, 1, 'asdf', {'a': 2}) == (1.0, 1, 'asdf', {'a': 2})