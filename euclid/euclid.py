def gcd(a, b):
    try:
        return gcd(b, a % b)
    except ZeroDivisionError:
        return a
