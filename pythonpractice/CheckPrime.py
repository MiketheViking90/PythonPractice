from pythonpractice.Divisors import get_divisors


def is_prime(n):
    divs = get_divisors(n)
    if len(divs) == 0:
        return True
    return False


print(is_prime(43))
print(is_prime(21))
print(is_prime(42))
