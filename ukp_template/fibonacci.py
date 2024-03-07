class Fibonacci:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        ##### YOUR CODE HERE #####
        if n <= 0:
            raise ValueError("You should enter a positive integer")
        if n == 1 or n == 2:
            return 1
        else:
            result = self.fib(n-1) + self.fib(n-2)
        return result
        ##########################