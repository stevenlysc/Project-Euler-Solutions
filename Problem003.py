#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

import time

def solution(number):
    if number == 1 or number == 0:
        return None
    n = 2
    while n ** 2 < number:
        if number % n == 0:
            number = number / n
        else:
            n = n + 1
    print 'The answer is {}' .format(number)

def main():
    start = time.clock()
    solution(600851475143)
    print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))

if __name__ == '__main__':
    main()
    
