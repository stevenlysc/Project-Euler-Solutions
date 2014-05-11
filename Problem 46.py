# -*- coding: utf-8 -*-
'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

from Utilities import get_prime_sieve, get_prime_truthtable

def main():
    prime_list = get_prime_sieve(10 ** 4)
    prime_truth = get_prime_truthtable(10 ** 4)
    composite = 0
    for i in xrange(3, 10 ** 5, 2):
        if not prime_truth[i]:
            square_num = 1
            while True:
                if i - 2 * square_num ** 2 > 1:
                    if not prime_truth[i - 2 * square_num ** 2]:
                        square_num += 1
                    else:
                        break
                else:
                    composite = i
                    break
        if composite != 0:
            break
    print composite

if __name__ == '__main__':
    main()