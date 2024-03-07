"""CLI interface for ukp_template project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
##### YOUR CODE HERE #####
import sys
from ukp_template.fibonacci import Fibonacci 
##########################

def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m ukp_template` and `$ ukp_template `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    ##### YOUR CODE HERE #####
    print("This will do something")
    n = sys.argv[1]
    fibo = Fibonacci()
    result = fibo.fib(n)
    print(result)
    ##########################