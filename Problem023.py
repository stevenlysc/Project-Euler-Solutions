#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import time

def divisorSum(n):
	divSum = 1
	for i in xrange(2, int(n ** 0.5) + 1):
		if n % i == 0:
			if n == i ** 2:
				divSum = divSum + i
			else:
				divSum = divSum + i + n/i
	return divSum

def solution():
	abundantList = set()
	notAbleSumList = set()
	for i in xrange(1, 28124):
		if divisorSum(i) > i:
			abundantList.add(i)
		if not any(i - j in abundantList for j in abundantList):
			notAbleSumList.add(i)
	print 'The answer is {}' .format(sum(notAbleSumList))

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
