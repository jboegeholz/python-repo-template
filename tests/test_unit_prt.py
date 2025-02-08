import pytest

from python_repo_template import add_two_ints


@pytest.mark.parametrize(
    "a, b, sum",
    [
        (1, 1, 2),
        (2, 2, 4),
    ]
)
def test_calculate_mean(a, b, sum):
    assert sum == add_two_ints(a, b)