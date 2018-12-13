import sys


def fib(n):
  if n < 0 or not isinstance(n, int):
    raise ValueError
  elif n < 2:
    return n
  return fib(n-1) + \
         fib(n-2)


def fib_argv():
    n=int(sys.argv[1])
    return fib(n)
