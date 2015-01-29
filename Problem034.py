#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math, time

def solution():
	factorial = [math.factorial(i) for i in xrange(10)]
	answer = 0
	# 9! * 6 = 2177280
	for i in xrange(3, 2177280):
		factSum = 0
		n = i
		while i > 0:
			d = i % 10
			i /= 10
			factSum += factorial[d]
		if factSum == n:
			answer += factSum
	print 'The answer is {}' .format(answer)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
