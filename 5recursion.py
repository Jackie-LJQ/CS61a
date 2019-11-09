def split(n):
    return n // 10, n % 10

def sum_digits(n):
    """return the sum of digits in n,
    recursion: in the body of function first use conditional statement to
    check for base case. Base case are evaluated without recursive call
    >>> sum_digits(204)
    6
    """
    if n < 10:
        return n
    all_but_last, last = split(n)
    return sum_digits(all_but_last) + last



def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


def luhn_sum(n):
    """mutual recursion: two function call each other"""
    if n < 10:
        return n
    all_but_last, last = split(n)
    return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    if n < 10:
        return sum_digits(2*n)
    else:
        all_but_last, last = split(n)
        double_sum = sum_digits(2*last)
        return luhn_sum(all_but_last) + double_sum

def sum_digits_ite(n):
    """find what state need to be maintain"""
    digits_sum = 0
    while n > 0:
        all_but_last, last = split(n)
        digit_sum = digits_sum + last
    return digit_sum

def sum_digits_rec(n, sum_digits):
    """let update become an argument"""
    if n==0:
        return sum_digits
    else:
        all_but_last, last = split(n)
        return sum_digits_rec(all_but_last, sum_digits + last)


def is_even(n):
    """use mutal recursion judge even or odd"""
    if n == 0:
        return True
    else:
        return is_odd(n-1)
def is_odd(n):
    if n == 1:
        return False
    else:
        return is_even(n-1)

def cascade(n):
    """
    >>>cascade(2019)
    2019
    201
    20
    2
    20
    201
    2019
    """
    print(n)
    if n > 10:
        print(n)
        cascade(n//10)
        print(n)



def play_alice(n):
    """play strategy"""
    if n==0:
        print('Bob wins')
    else:
        return play_bob(n-1)

def play_bob(n):
    if n == 0:
        print('Alice wins')
    elif is_even(n):
        return play_alice(n-2)
    else:
        return play_alice(n-1)
