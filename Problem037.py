#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import time

def getPrimeTable(scope):
	primeList = [1] * scope
	for i in xrange(2, int(scope ** .5) + 1):
		if primeList[i] == 1:
			for m in xrange(i ** 2, scope, i):
				primeList[m] = 0
	primeList[0], primeList[1] = 0, 0
	return primeList

def trunNumbers(number):
	leftTrun, rightTrun = number, number
	truList = list()
	tmp = 10
	while rightTrun / tmp != 0:
		truList.append(rightTrun / tmp)
		tmp *= 10
	tmp = 10
	while leftTrun % tmp != leftTrun:
		truList.append(leftTrun % tmp)
		tmp *= 10
	return truList

def solution():
	count = 0
	answer = 0
	tmp = 10
	primes = getPrimeTable(10 ** 6)
	while count < 11:
		flag = 0
		if primes[tmp]:
			for t in trunNumbers(tmp):
				if not primes[t]:
					flag = 1
			if not flag:
				count += 1
				answer += tmp
		tmp += 1
	print 'The answer is {}' .format(answer)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
