# -*- coding: utf-8 -*-
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from Utilities import get_prime_truthtable, circular_number

def main():
    prime_list = get_prime_truthtable(10 ** 6)
    count = 0
    for i in xrange(2, 10 ** 6):
        flag = 0
        if prime_list[i] == 1:
            for j in circular_number(i):
                if prime_list[j] == 0:
                    flag = 1
            if not flag:
                count += 1
    print count

if __name__ == '__main__':
    main()