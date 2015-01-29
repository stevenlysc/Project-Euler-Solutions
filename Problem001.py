#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import time

def solution():
    answer = sum(set(range(3, 1000, 3) + range(5, 1000, 5)))
    print 'The answer is {}'.format(answer)
    return

def main():
    start = time.clock()
    solution()
    print 'Elasped: {} ms' .format(1000 * (time.clock() - start))

if __name__ == '__main__':
    main()
