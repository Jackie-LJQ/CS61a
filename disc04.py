def count_stair_ways(n):
    """go up a stairs that has n steps, once can take one or two steps
    find num of ways can go up this stair
    """
    assert n > 0, 'input should be a postive num'
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def count_k(n,k):
    """climb n stairs, once can take up to k steps, include k
    find how many ways
    >>> count_k(3,3)  #3, 2+1, 1+2, 1+1+1
    4
    >>> count_k(10,3)
    274
    """
    if n < 0:
        return 0
    elif n==0:
        return 1
    return sum([count_k(n-i, k) for i in range(1, k + 1)])

def even_weighted(x):
    """choose even index elements in x and multiply each element by its index
    return this new list
    >>> x = [1,2,3,4,5,6]
    >>> even_weighted(x)
    [0,6,20]
    """
    return [i * x[i] for i in range(len(x)) if i%2==0]

def max_product(x):
    """find the maximul product of unconsecutive elements in list x
    >>> max_product([10,3,1,9,2]) #10*9
    90
    >>> max_product([5,10,5,10,5]) #5*5*5
    125
    """
    if len(x) == 0:
        return 1
    elif len(x) <= 2:
        return max(x)
    return max([x[i] * max_product(x[i+2:]) for i in range(len(x))])

def max_product1(x):
    if len(x) == 0:
        return 1
    elif len(x) == 1:
        return x[0]
    return max(max_product1(x[1:]), x[0] * max_product1(x[2:]))
