#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time

def isPalindromic(x):
    return str(x)[:] == str(x)[::-1]

def solution():
    answer = list()

    for i in range(100, 1000):
        for j in range(i, 1000):
            if isPalindromic(i * j):
                answer.append(i * j)

    print 'The answer is {}' .format(max(answer))
    return

def main():
    start = time.clock()
    solution()
    print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
    main()
