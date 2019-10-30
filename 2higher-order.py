from operator import add
"""1.compute fibonacci number
    >>> a=fib(7)
    >>> a
    8
"""
def fib(n):
    i=0
    j=k=1
    while k<n:
        i,j=j,add(i,j)
        k=k+1
    return i


"""2.calculate the area of circle(pi), square(1) and hexagon(3*sqrt(3)/2)"""
from math import sqrt, pi
def area(r,shape_constant):
    assert r>0, 'A length must be positive'
    return r*r*shape_constant

"""3.generalize funcation"""
def summation(n,term):
    """
    >>> summation(5,identity)
    15
    >>> summation(5,cube)
    225
    """
    i,total=1,0
    while i<=n:
        total,i= term(i)+total,i+1
    return total
def cube(x):
    return pow(x,3)
def identity(x):
    return x
def pi_term(x):
    return 8 / mul(k * 4 - 3, k * 4 - 1)

"""return value is f unction"""
def make_adder(n):
    """
    >>> make_adder(2013)(6)
    2019
    >>> f=make_adder(2013)
    >>> f(6)
    2019
    """
    def adder(k):
        return k+n
    return adder
