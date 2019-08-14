import math

def get_divisors(n):
    sqrt = int(math.sqrt(n))
    divs = []
    for x in range(2, sqrt, 1):
        if (n%x == 0):
            divs.append(x)
            divs.append(int(n/x))
    divs.sort()
    return divs

divs = get_divisors(240)
print(*divs, sep=",")