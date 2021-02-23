"""
Fibonacci code
"""

from typing import Dict
from functools import lru_cache
from typing import Generator


# Would cause infinte recursion there is no base case
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib2(n - 1) + fib2(n - 2)


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


# Use memoization for efficiency
memo: dict = {0: 0, 1: 1}


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


# Automatic memoization
@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)


# for loop is still most performant

def fib5(n : int )-> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for i in range(1, n):
        last, next = next, last + next
    return next

# Lets do it with a generator
def fin_gener(n : int ) -> int:
    yield 0
    if n > 1:
        yield 1
    last : int = 0
    next : int = 1
    for _ in range(1, n ):
        last, next = next, next + last
        yield next

if __name__ == "__main__":
    for i in fin_gener(50):
        print(i)
