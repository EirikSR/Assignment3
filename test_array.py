test = "er"
shape = (3,)


def test_string():
    assert isinstance(Array.print(), str)


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [([shape, 3, 2, 5], [shape, 3, 2, 1]), [6, 4, 6]],
        [([shape, 4, 2, 2], [shape, 2, 1, 3]), [6, 3, 5]],
        [([shape, 6, 6, 7], [shape, 4, 0, 2]), [10, 6, 9]],
    ],
)
def test_add(arg, expected_output):
    assert (Array(arg[0]) + Array(arg[1])) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [([shape, 3, 2, 5], [shape, 3, 2, 1]), [0, 0, 4]],
        [([shape, 4, 2, 2], [shape, 2, 1, 3]), [2, 1, -1]],
        [([shape, 6, 6, 7], [shape, 4, 0, 2]), [2, 6, 5]],
    ],
)
def test_sub(arg, expected_output):
    assert (Array(arg[0]) - Array(arg[1])) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [([shape, 3, 2, 5], 2), [6, 4, 10]],
        [([shape, 4, 2, 2], Array([shape, 2, 1, 3])), [8, 2, 6]],
        [([shape, 6, 6, 7], -1), [-6, -6, -7]],
    ],
)
def test_mul(arg, expected_output):
    assert (Array(arg[0]) - arg[1] == expected_output

@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [([shape, 3, 2, 5], [shape, 3, 2, 5]), True],
        [([shape, 4, 2, 2], [shape, 2, 1, 3]), False],
        [([shape, 6, 6, 7], [shape, 6, 6, 7]), True],
    ],
)
def test_equal(arg, expected_output):
    assert (Array(arg[0]) == Array(arg[1])) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [([shape, 3, 2, 5], [Array(shape, 3, 2, 5)]), [True, True, True]],
        [([shape, 4, 2, 2], [Array(shape, 2, 2, 3)]), [False, True, False]],
        [([shape, 6, 6, 7], 6, [True, True, False]],
    ],
)
def test_isequal(arg, expected_output):
    assert (Array(arg[0]) == arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [[shape, 3, 2, 4], 3],
        [[shape, 4, 2, 2], 8./3],
        [[shape, 6, 6, 7], 19./3],
    ],
)
def test_mean(arg, expected_output):
    assert Array(arg).mean() - expected_output < margin


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [[shape, 3, 2, 4], 0.66666666666667],
        [[shape, 4, 2, 2], 0.88888888888889],
        [[shape, 6, 6, 7], 0.22222222222222],
    ],
)
def test_variance(arg, expected_output):
    assert Array(arg).variance() - expected_output < 1E-8


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [[shape, 3, 2, 4], 2],
        [[shape, 4, 2, 2], 2],
        [[shape, 6, 6.1, 7], 6],
    ],
)
def test_min_element(arg, expected_output):
    assert Array(arg).min_element() - expected_output < 1E-8

