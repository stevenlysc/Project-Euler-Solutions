# -*- coding: utf-8 -*-
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from Utilities import is_prime

def main():
    count = 0
    working = 1
    while count < 10001:
        working += 1
        if is_prime(working):
            count += 1
    print working

if __name__ == '__main__':
    main()