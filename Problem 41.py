# -*- coding: utf-8 -*-
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from Utilities import get_prime_sieve, pandigital_number

def main():
    prime_list = get_prime_sieve(10000000)[::-1]
    for i in prime_list:
        if pandigital_number(i):
            return i

if __name__ == '__main__':
    print main()