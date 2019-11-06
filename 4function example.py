from operator import add
def make_adder(x):
    def adder(y):
        return x + y
    return adder
#add(x, y)
"""the difference between add and make_adder is that
add takes two argument and give back their sum
make_adder takes one argument and return a function"""


def carry2(f):
    """manipulate functions use lambda
    transfer a multi-arguments function into a one argument higher order function"""
    return lambda x: lambda y: f(x,y)

def trace(fn):
    def traced(x):
        print('calling function', fn, 'at argument', x)
        return fn(x)
    return traced

@trace
def square(x):
    return x * x

@trace
def sum_square_up_to(n):
    k, sum = 1, 0
    while k < n:
        sum, k = sum + square(k), k + 1

#output practice
def pirate(argg):
    print('matey')
    def plunder(argg):
        return argg
    return plunder
"""find parameter in the closest frame"""

def delay(arg):
    print('delayed')
    def g():
        return arg
    return g

def remove(n, digit):
    kept, digits = 0, 0
    while n > 0:
        n, last = n//10, n % 10
        if last!=digit:
            kept = last*pow(10,digits) + kept
            digits = digits + 1
    return kept
