def count_digits(n):
    """
    1.count digits in that number
    >>> count_digits(4)
    1
    >>> count_digits(12345678)
    8
    >>> count_digits(0)
    0
    """
    i, k = 0, n
    while k > 0:
        i, k = i + 1, k//10
    return i



def count_matches(n, m):
    '''
    2.count match digits
    >>> count_matches(10, 30)
    1
    >>> count_matches(12345, 23456)
    0
    >>> count_matches(121212, 123123)
    2
    >>> count_matches(111, 11) # only one's place matches
    2
    >>> count_matches(101, 10) # no place matches
    0
    '''
    num_match = 0
    while m > 0 and n > 0:
        last_n, last_m = n % 10, m % 10
        if last_n == last_m:
            num_match+=1
        n, m = n//10, m//10
        k= min(n,m)
    return num_match

def foo(x):
    def f(y):
        def g(z):
            return x + y * z
        return g
    return f

foo = lambda x: lambda y: lambda z: x + y * z


def make_skipper(n):
    """
    3.print number between 0 and x and skip nth number
    >>> a = make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    def range(x):
        i = 1
        while i <= x:
            if i % n:
                print (i)
            i+=1
    return range



def is_even(x):
    return x % 2 == 0

def keep_ints(cond, n):
    """
    4.print 1...i...n where cond(i) is true
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i = i + 1



def make_keeper(n):
    """
    5.higher order function like keep_ints
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def rules(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i = i + 1
    return rules
