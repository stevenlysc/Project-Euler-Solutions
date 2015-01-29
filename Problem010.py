#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import time

def get_prime_truthtable(scope):
    '''Return the turthtable of the prime numbers'''
    index = [1] * scope
    for i in xrange(2, int(scope ** 0.5) + 1):
        if index[i]:
            for m in xrange(i ** 2, scope, i):
                index[m] = 0
    index[0], index[1] = 0, 0
    return index

def solution():
    answer = 0
    truthTable = get_prime_truthtable(2 * 10 ** 6)
   
    for i in xrange(len(truthTable)):
        if truthTable[i]:
            answer = answer + i

    print 'The answer is {}' .format(answer)

def main():
    start = time.clock()
    solution()
    print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
    main()
