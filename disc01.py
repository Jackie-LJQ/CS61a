def wear_jacket_with_if(temp, raining):
    """will wear jacket when temperature is lower than 60 or raining"""
    if raining or temp < 60:
        return ture
    return False

def wear_jacket(temp, raining):
    return raining or temp < 60

def is_prime(n):
    i = 2
    if n==1:
        return False
    while i < n:
        if n % i==0:
            return False
        i+=1
    return True
