def multiply(m,n):
    if n == 1:
        return m
    else:
        return multiply(m, n-1) + m



def hailstone(n):
    def count(n, i):
        print(n)
        if n==1:
            return i
        elif n % 2==0:
            return count(n//2, i + 1)
        else:
            return count(n*3 + 1, i + 1)
    return count(n, i = 1)

def hailstone2(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone2(n//2)
    else:
        return 1 + hailstone2(n*3 + 1)



def is_prime(n):
    """use recursion find whether a num is a prime num"""
    def count(k, i):
        if k == n:
            return i
        elif n % k == 0:
            return count(k+1, i+1)
        else:
            return count(k+1, i)
    return count(1, 1) == 2

def is_prime2(n):
    def prime_helper(index):
        if index == n:
            return True
        elif n % index == 0 or n==1:
            return False
        else:
            return prime_helper(index+1)
    return prime_helper(2)




def merge(n1, n2):
    """n1, n2 is number with decreasing order digits,
    return a single number with decreasing order digits"""
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1//10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2//10) * 10 + n2 % 10




def make_func_repeater(f, n):
    if n==1:
        return f
    else:
        return make_func_repeater(lambda x: f(f(x)), n-1)
