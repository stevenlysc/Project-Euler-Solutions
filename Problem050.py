#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import time

def getPrimeTruthTable(scope):
	primes = [1] * scope
	for i in xrange(2, int(scope ** .5) + 1):
		if primes[i]:
			for m in xrange(i ** 2, scope, i):
				primes[m] = 0
	primes[0], primes[1] = 0, 0
	return primes

def getPrimes(scope):
	tmp = getPrimeTruthTable(scope)
	primes = list()
	for i in xrange(len(tmp)):
		if tmp[i]:
			primes.append(i)
	return primes

def solution():
	primes = getPrimes(5 * 10 ** 5)
	primeTruthTable = getPrimeTruthTable(10 ** 6)
	count, total = 0, 0
	for i in xrange(len(primes) - 2):
		tmpCount = 1
		tmpTotal = primes[i]
		while tmpTotal < 10 ** 6:
			i += 1
			tmpTotal += primes[i]
			tmpCount += 1
		tmpTotal = tmpTotal - primes[i]
		if primeTruthTable[tmpTotal] and tmpCount > count:
			count = tmpCount
			total = tmpTotal
	print 'The answer is {}' .format(total)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
