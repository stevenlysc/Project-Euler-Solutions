# -*- coding: utf-8 -*-
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from Utilities import get_prime_sieve

def main():
    print sum(get_prime_sieve(2 * 10 ** 6))


if __name__ == '__main__':
    main()