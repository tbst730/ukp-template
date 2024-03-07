import pytest
from ukp_template import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from ukp_template import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####
def test_negative():
    Fibo = Fibonacci()
    with pytest.raises(ValueError):
        Fibo.fib(n=-1)

def test_fibonacchi():
    Fibo = Fibonacci()
    assert Fibo.fib(n=5) == 5
##########################