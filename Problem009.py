#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time

def isPythagoreanTriplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2

def solution():
    for a in xrange(1, 1001):
        for b in xrange(1, 1000 - a + 1):
                if isPythagoreanTriplet(a, b, 1000 - a - b):
                    print 'The answer is {}' .format(a * b * (1000 - a - b))
                    return

def main():
    start = time.clock()
    solution()
    print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
    main()
