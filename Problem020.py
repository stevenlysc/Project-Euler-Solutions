#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import time
from math import factorial

def solution():
	tmp = factorial(100)
	tmpStr = str(tmp)
	answer = 0
	for i in xrange(len(tmpStr)):
		answer += int(tmpStr[i])
	print 'The answer is {}' .format(answer)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
