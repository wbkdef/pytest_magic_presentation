import sys
import pytest
from fcns import \
    fib, fib_argv

# It's important that
# this file's and
# function's names
# both start with "test_"
# This is how pytest
# knows it's a test.
@pytest.mark.slow
def test_fib_base():
    assert fib(0) == 0
    assert fib(1) == 1


def test_fib_ind():
    assert fib(3) == 2
    assert fib(6) == 9

# We run the same test, multiple times
# with different values
@pytest.mark.parametrize("arg, val", [
    (3, 2),
    (4, 3),
    (5, 6),
    (6, 8),
], ids=repr)
def test_fib_ind(arg, val):
    assert fib(arg) == val



@pytest.mark.parametrize("n", [
    -1, -2, -10,
    3.6, 1.1, 3
],ids=repr)
def test_fib_raise(n):
    # Will fail the test UNLESS
    # a ValueError is raised
    with pytest.raises(ValueError):
        fib(n)

# We can do targetted
# setup/teardown
# with fixtures
@pytest.fixture()
def argv6():
    sa = sys.argv
    try:
        sys.argv = ["", "6"]
        yield sys.argv
    finally:
        sys.argv = sa
def test_fib_argv(argv6):
    print(argv6)
    assert fib_argv()==13

