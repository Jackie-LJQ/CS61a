from operator import floordiv,mod
def div_n_d(w,v):

    """return the quation and remainder of dividing w by v
    >>> a,b=div_n_d(5,3)
    >>> a
    1
    >>> b
    2
    """
    return floordiv(w,v), mod(w,v)

def absoluate_value(x):
    """return the absoluate value of x
    >>> a=absoluate_value(0)
    >>> a
    0
    >>> b=absoluate_value(2)
    >>> b
    2
    >>> c=absoluate_value(-2)
    >>> c
    2
    """
    if x>0:
        return x
    elif x==0:
        return 0
    else:
        return -x
