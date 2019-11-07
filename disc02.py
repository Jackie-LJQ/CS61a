curry2 = lambda h: lambda x: lambda y: h(x, y)

def keep_int(cond, n):
    """print all n that satisfies cond"""
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i+=1

def is_even(x):
    return x % 2 == 0

keep_int(is_even, 5)

def keep_int1(n):
    """change keep_int to a higher order function"""
    def is_print(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i+=1
    return is_print



def and_add(f, n):
    def h(x):
        return f(x) + n
    return h
