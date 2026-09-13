# Reduce method
import functools as f


def mul(a, b):
    return a * b


print(f.reduce(mul, l))

