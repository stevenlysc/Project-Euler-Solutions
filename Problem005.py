#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import time

def solution(n):
    numbers = range(1, n+1)[::-1]
    answer = 1

    while not numbers == []:
        pop = numbers.pop()
        answer = answer * pop
        for i in xrange(len(numbers)):
            if numbers[i] % pop == 0:
                numbers[i] = numbers[i] / pop

    print 'The answer is {}' .format(answer)

def main():
    start = time.clock()
    solution(20)
    print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
    main()
