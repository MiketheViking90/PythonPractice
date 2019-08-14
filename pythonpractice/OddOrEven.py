def even_or_odd(n):
    msg = str(n) + " is : "
    if (n % 4 == 0):
        print("multiple of 4")
    elif (n%2 == 0):
        print(msg + "odd")
    else:
        print(msg + "even")

def isDivisor(n, d):
    if (n%d == 0):
        print("%d divides %d" % (n, d))
    else:
        print("no divisor")

even_or_odd(12)
even_or_odd(10)
even_or_odd(9)

isDivisor(10, 2)
isDivisor(10, 3)