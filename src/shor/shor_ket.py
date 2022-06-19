from math import gcd, isqrt, pow, log2, ceil
from random import randint, seed

from ket import *
from ket.plugins import pown
from ket.lib import qft

seed(47)


def shor_factors(n: int) -> (int, int):
    if (n % 2 == 0):
        return (2, n // 2)

    n_sqrt = isqrt(n)
    # TODO: check this
    for i in range(2, n_sqrt + 1):
        pow_ = pow(n, 1 / i)
        if (pow_ % 1 == 0):
            pow_ = int(pow_)
            return (pow_, n // pow_)

    while True:
        a = randint(2, n)
        gcd_a_n = gcd(a, n)
        if (gcd_a_n > 1):
            return (gcd_a_n, n // gcd_a_n)

        size: int = ceil(log2(n + 1))
        reg1 = quant(size)
        reg2 = quant(size)
        H(reg1)
        pown(a, reg1 + reg2, n)
        measure(reg2)
        qft(reg1)
        r = measure(reg1).value
        if (r % 2 == 0):
            p = gcd(a**(r//2) - 1, n)
            q = gcd(a**(r//2) + 1, n)
            if (p != 1 and q != 1):
                return (p, q)


for i in range(2, 100):
    try:
        p, q = shor_factors(i)
        if (p * q != i):
            print(f"error: {p} * {q} != {i}")
        else:
            print(f"{p} * {q} = {i}")
    except TypeError as e:
        print(f"{e} with n = {i}")
        break
