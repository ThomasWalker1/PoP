def isprime(p):
    from math import sqrt, ceil
    if p == 1:
        return False
    elif p == 2:
        return True
    for i in range(2, ceil(sqrt(p))+1):
        if p % i == 0:
            return False
    return True
