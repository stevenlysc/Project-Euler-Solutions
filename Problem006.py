#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

import time

def solution(n):
    sum_of_square = sum([i ** 2 for i in xrange(1, n+1)])
    square_of_sum = sum([i for i in xrange(1, n+1)]) ** 2
    answer = square_of_sum - sum_of_square

    print 'The answer is {}' .format(answer)

def main():
    start = time.clock()
    solution(100)
    print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
    main()
