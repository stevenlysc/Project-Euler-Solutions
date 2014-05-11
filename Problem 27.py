# -*- coding: utf-8 -*-
'''
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

from Utilities import get_prime_truthtable

def func_n(n, a, b):
    return max(n ** 2 + a * n + b, 0)

def main():
    countMax = 0
    stroreProd = 0
    prime_truth = get_prime_truthtable(10**5)
    for b in xrange(1, 1000, 2):
        if prime_truth[b]:
            for a in xrange(-b, 1000, 2):
                if prime_truth[1 + a + b]:
                    for n in xrange(2, 1000):
                        #print func_n(n, a, b), n, a, b, '---'
                        if not prime_truth[func_n(n, a, b)]:
                            if n > countMax:
                                countMax = n
                                stroreProd = a * b
                            #print func_n(n, a, b), n, a, b, '---out'
                            break
    print stroreProd

if __name__ == '__main__':
    main()