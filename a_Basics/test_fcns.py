import sys
from fcns import \
    fib, fib_argv

# It's important that
# this file's and
# function's names
# both start with "test_"
# This is how pytest
# knows it's a test.
def test_fib_base():
    assert fib(0) == 0
    assert fib(1) == 1
def test_fib_ind():
    assert fib(3) == 2
    assert fib(6) == 9
def test_fib_raise():
    fib(-1)
    fib(3.6)

def test_fib_argv():
    sa = sys.argv
    sys.argv = ["", "6"]
    assert fib_argv()==13
    sys.argv = sa

