#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import time

def isPrime(x):
    for i in xrange(2, int( x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution():
    count, number = 0, 1
    
    while count != 10001:
        number = number + 1
        if isPrime(number):
            count = count + 1

    print 'The answer is {}' .format(number)

def main():
    start = time.clock()
    solution()
    print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
    main()
