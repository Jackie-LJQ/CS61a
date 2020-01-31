def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1)+fib(n-2)

def count(f):
    # calculate complexity
    def counted(*argu):
        counted.call_count += 1
        return f(*argu)
    counted.call_count = 0
    return counted

# calculate the complexity of fib function
fib = count(fib)
fib(5)
coplex = fib.call_count

def count_frame(f):
    def counted(*argu):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*argu)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted
fib = count_frame(f)
fib(5)
frame = fib.max_count

# memoization
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cach:
            cache[n] = f(n)
        return cache[n]
    return memorized
fib = memo(fib)
