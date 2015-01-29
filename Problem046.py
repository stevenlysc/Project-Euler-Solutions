#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

import time

def isTwiceSquare(number):
	tmp = (number / 2) ** .5
	return tmp == int(tmp)

def getPrimeTable(scope):
	tmpList = [1] * scope
	primeList = []
	for i in xrange(2, int(scope ** .5) + 1):
		if tmpList[i]:
			for m in xrange(i ** 2, scope, i):
				tmpList[m] = 0
	tmpList[0], tmpList[1] = 0, 0
	for i in xrange(len(tmpList)):
		if tmpList[i]:
			primeList.append(i)
	return primeList

def solution():
	primes = getPrimeTable(10000)
	for i in xrange(3, 10000, 2):
		flag = 0
		if not i in primes:
			for j in primes:
				if i > j:
					if isTwiceSquare(i - j):
						flag = 1
			if not flag:
				print 'The answer is {}' .format(i)
				break

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
