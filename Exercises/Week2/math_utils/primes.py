def isprime(p):
    from math import sqrt, floor
    for i in range(1, floor(sqrt(p))+1):
        if p & i == 0:
            return False
    return True
