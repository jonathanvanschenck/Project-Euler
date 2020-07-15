"""


Created By: Jonathan D. B. Van Schenck

Method:

"""

from math import sqrt

def square_factor(number):
    n = 2
    ns = 4
    dividend = 1*number
    sq_fact = []
    while ns <= dividend:
        if dividend % ns == 0:
            sq_fact.append(n)
            dividend = dividend // ns
        else:
            ns = ns + 2 * n + 1
            n += 1
    return sq_fact, dividend

def power_set(iterable):
    # adapted from https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
    length = len(iterable)
    bit_masks = [1 << i for i in range(length)] # [b1, b10, b100, ... ]
    for i in range((1 << length) - 0):
        yield [elem for bit_mask, elem in zip(bit_masks, iterable) if bit_mask & i]

def product(iterable):
    prod = 1
    for i in iterable:
        prod *= i
    return prod

D_set = set()
target_length = 100 - int(sqrt(100))
x = 1
while len(D_set) < target_length:
    x += 1
    sq_facts, _D = square_factor(x**2 - 1)
    if _D == 1:
        # print(_D)
        D_set.add(_D)
    else:
        for subset in power_set(sq_facts):
            D = _D * product(subset)**2
            if D <= 100:
                # print(D,subset,_D)
                D_set.add(D)
