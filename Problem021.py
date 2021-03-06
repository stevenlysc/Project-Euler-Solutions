#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import time

def divisorSum(n):
	divSum = 1
	for i in xrange(2, int(n ** 0.5) + 1):
		if n % i == 0:
			if n == i ** 2:
				divSum += i
			else:
				divSum = divSum + i + n/i
	return divSum

def solution():
	answer = 0
	for i in xrange(2, 10001):
		if divisorSum(divisorSum(i)) == i and divisorSum(i) != i:
			answer += i
	print 'The answer is {}' .format(answer)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
