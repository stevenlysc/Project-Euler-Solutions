#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

import time

def isPandigital(x, y):
	panSet = set(str(x)[:] + str(y)[:] + str(x*y)[:])
	panSet.add('0')
	return True if len(panSet) == 10 else False

def solution():
	numSet = set()
	# the searching space can be limited to a quite small area, for more details:
	# http://www.mathblog.dk/project-euler-32-pandigital-products/
	for a in xrange(2, 100):
		bStart = 123 if a > 9 else 1234
		bEnd = 10000 / a
		for b in xrange(bStart, bEnd + 1):
			if isPandigital(a, b):
				numSet.add(a * b)
	print 'The answer is {}' .format(sum(numSet))

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
