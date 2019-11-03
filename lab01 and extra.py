"""Lab 1: Expressions and Control Structures"""

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0 # You can replace this line!

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    sum=0
    while n > 0:
        sum, n = sum + n%10, n//10
    return sum


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
