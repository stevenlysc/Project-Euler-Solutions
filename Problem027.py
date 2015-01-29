#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

import time

def formula(n, a, b):
	return n ** 2 + a * n + b

def  primeTruthTable(length):
	truthTable = [1 for i in xrange(length)]
	for i in xrange(2, int(length ** 0.5) + 1):
		if truthTable[i] == 1:
			for m in xrange(i ** 2, length, i):
				truthTable[m] = 0
	truthTable[0], truthTable[1] = 0, 0
	return truthTable

def solution():
	primeTable = primeTruthTable(10 ** 5)
	count, maxProd = 0, 0
	# the primes have to be positive, so b > 0 and a > -b-1 according to the fomular
	# also primes cannot be even numbers, so b has to be odd, so is a
	for b in xrange(1, 1000, 2):
		if primeTable[b]:
			for a in xrange(-b, 1000, 2):
				if primeTable[1 + a + b] and primeTable[4 + 2 * a + b]:
					for n in xrange(3, 1000):
						if not primeTable[formula(n, a, b)]:
							if n > count:
								count = n
								maxProd = a * b
							break
	print 'The answer is {}' .format(maxProd)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
