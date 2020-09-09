import Array as a
import pytest

test = "er"
shape = (3,)


def test_string():
    assert isinstance(a.Array(shape, 1, 2, 3).__str__(), str) == True


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), a.Array(shape, 3, 2, 1)), [6, 4, 6]],
        [(a.Array(shape, 4, 2, 2), a.Array(shape, 2, 1, 3)), [6, 3, 5]],
        [(a.Array(shape, 6, 6, 7), a.Array(shape, 4, 0, 2)), [10, 6, 9]],
    ],
)
def test_add(arg, expected_output):
    assert arg[0] + arg[1] == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), a.Array(shape, 3, 2, 1)), [0, 0, 4]],
        [(a.Array(shape, 4, 2, 2), a.Array(shape, 2, 1, 3)), [2, 1, -1]],
        [(a.Array(shape, 6, 6, 7), a.Array(shape, 4, 0, 2)), [2, 6, 5]],
    ],
)
def test_sub(arg, expected_output):
    assert arg[0] - arg[1] == expected_output


@ pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), 2), [6, 4, 10]],
        [(a.Array(shape, 4, 2, 2), a.Array(a.Array(shape, 2, 1, 3)), [8, 2, 6]],
        [(a.Array(shape, 6, 6, 7), -1), [-6, -6, -7]],
    ],)
def test_mul(arg, expected_output):
    assert (arg[0] - arg[1]) == expected_output

@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), a.Array(shape, 3, 2, 5), True],
        [(a.Array(shape, 4, 2, 2), a.Array(shape, 2, 1, 3), False],
        [(a.Array(shape, 6, 6, 7), a.Array(shape, 6, 6, 7), True],
    ],)
def test_equal(arg, expected_output):
    assert (arg[0] == arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), [a.Array(shape, 3, 2, 5)), [True, True, True]],
        [(a.Array(shape, 4, 2, 2), [a.Array(shape, 2, 2, 3)), [False, True, False]],
        [(a.Array(shape, 6, 6, 7), 6), [True, True, False]],
    ],)
def test_isequal(arg, expected_output):
    assert (arg[0) == arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
        [[a.Array(shape, 3, 2, 4), 3], 
        [a.Array(shape, 4, 2, 2), 8.0 / 3], 
        [a.Array(shape, 6, 6, 7), 19.0 / 3]
    ],)
def test_mean(arg, expected_output):
    assert a.Array(arg).mean() - expected_output < margin


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [a.Array(shape, 3, 2, 4), 0.66666666666667],
        [a.Array(shape, 4, 2, 2), 0.88888888888889],
        [a.Array(shape, 6, 6, 7), 0.22222222222222],
    ],)
def test_variance(arg, expected_output):
    assert arg.variance() - expected_output < 1e-8


@pytest.mark.parametrize(
    "arg, expected_output",
        [[a.Array(shape, 3, 2, 4), 2],
        [a.Array(shape, 4, 2, 2), 2],
        [a.Array(shape, 6, 6.1, 7), 6]
    ],)
def test_min_element(arg, expected_output):
    assert arg.min_element() - expected_output < 1e-8
