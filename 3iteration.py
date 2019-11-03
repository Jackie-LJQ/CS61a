def end(n,d):
    """print the final digit of n in reverse order until d is fuond
    >>> end(98789, 8)
    98
    >>> end(17689654, 9)
    4569
    >>> end(89,9)
    9
    >>> end(9,1)
    9
    >>> end(987,6)
    789
    """
    t = 0
    while n > 0:
        last, n = n%10, n//10
        t = last + t * 10
        if last == d:
            return t
    return t


def is_three(x):
    return x==3
def square(x):
    return max(0, x*x-100)
def search(f):
    """find the smallest x that makes function f is true
    >>> search(is_three)
    3
    >>> search(square)
    11
    """
    x = 0
    while not f(x):
        x += 1
    return x

def inverse(f):
    """find g -> g(f(x))=x"""
    def search_inverse(y):
        x=0
        while True:
            if f(x)==y:
                return x
            else: x+=1
    return search_inverse

def square(x):
    return x*x

def search_inverse(f):
    """find inverse function of f, easy code"""
    return lambda y:search(lambda x: y==f(x))

def print_all(x):
    """function refer to itself"""
    print(x)
    return print_all

def print_sum(x):
"""print sum of oprands"""
    print(x)
    def next_sum(y):
        return print_sum(x+y)
    return next_sum
print_sum(1)(2)(3)

from math import sqrt
def if_function(x,y,z):
    """difference between call expression and if """
    if x:
        return y
    else:
        return z

def squr_real(x):
    if x > 0:
        return sqrt(x)
    else:
        return 0

def squr_real1(x):
    """ this function crush because when excuate a function, all operands are evaluated"""
    return if_function(x>0, sqrt(x), 0)

"""use and, or to avoid crush"""
def has_squr_root(x):
    return x>0 and sqrt(x)

def resonable(n):
    return n==0 or 1/n != 0

abs(x=1/x if x!=0 else 0)"""condition expression"""
