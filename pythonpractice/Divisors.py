import math

def getDivisors(n):
    sqrt = int(math.sqrt(n))
    divs = []
    for x in range(2, sqrt, 1):
        if (n%x == 0):
            divs.append(x)
            divs.append(int(n/x))
    divs.sort()
    return divs

divs = getDivisors(240)
print(*divs, sep=",")