import pytest

from solution import solve


@pytest.mark.parametrize(
    "args, expected",
    [
        # (input, expected) rows derived from README examples + edge cases
    ],
)
def test_cases(args, expected):
    assert solve(*args) == expected
