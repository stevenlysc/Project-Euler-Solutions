#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

import time

def sumOfPowers(number, kth):
	powerSum = 0
	for i in xrange(len(str(number))):
		powerSum += int(str(number)[i]) ** kth
	return powerSum

def solution():
	sumNum = 0
	for number in xrange(1, 295245):
		if 1 == number:
			pass
		elif sumOfPowers(number, 5) == number:
			sumNum += number
	print 'The answer is {}' .format(sumNum)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
