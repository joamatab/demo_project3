"""dp - demo project"""

__version__ = "0.0.3"
__author__ = "your_name <your_email@gmail.com>"


def fibonacci(n):
    """Return the nth number in the Fibonacci sequence."""
    if n < 0:
        raise ValueError("n must be >= 0")
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
