#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

import time

def getPrimeTable(scope):
	tmp = [1] * scope
	primes = []
	for i in xrange(2, int(scope ** .5) + 1):
		if tmp[i]:
			for m in xrange(i ** 2, scope, i):
				tmp[m] = 0
	tmp[0], tmp[1] = 0, 0
	for i in xrange(len(tmp)):
		if tmp[i]:
			primes.append(i)
	return primes

def primeFactorNumbers(number, primes):
	count = 0
	for i in primes:
		flag = 0
		while number % i == 0:
			number /= i
			if flag == 0:
				count += 1
				flag = 1
		if number == 1:
			break
	return count

def solution():
	count = 0
	primes = getPrimeTable(10000)
	for i in xrange(646, 1000000):
		if primeFactorNumbers(i, primes) == 4:
			count += 1
		else:
			count = 0
		if count == 4:
			print 'The answer is {}' .format(i - 3)
			break

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
