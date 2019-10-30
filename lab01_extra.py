"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total, stop=1, n-k
    while n > stop:
        total, n=total*n, n-1
    return total


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    while n > 10:
        if n % 10==8:
            n=n//10
            if n % 10==8:
                return True
            else:
                n=n//10
        else:
            n=n//10
    return False

"""another approach"""
def double_eights1(n):
    """Return true if n has two eights in a row.
    >>> double_eights1(8)
    False
    >>> double_eights1(88)
    True
    >>> double_eights1(2882)
    True
    >>> double_eights1(880088)
    True
    >>> double_eights1(12345)
    False
    >>> double_eights1(80808080)
    False
    """
    previous=False
    while n % 10 > 0:
        if n % 10 == 8 and previous:
            return True
        elif n % 10 ==8:
            previous = True
        else:
            previous = False
        n = n//10
    return False
