# -*- coding: utf-8 -*-
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from Utilities import pythagorean_triplet

def main():
    for a in xrange(1, 1000):
        for b in xrange(a, 1000 - a):
            if pythagorean_triplet(a, b, 1000 - a - b):
                print a * b * (1000 - a - b)
                break


if __name__ == '__main__':
    main()