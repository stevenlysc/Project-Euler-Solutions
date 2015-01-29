#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import time
from math import factorial

def lexiPermutation(nth):
	ith = 0
	permutation = list()
	i, digit = -1, 1
	while ith < nth:
		i = i + 1
		while i in permutation:
			i = i + 1
		ith = ith + factorial(10 - digit)
		if ith > nth:
			ith = ith - factorial(10 - digit)
			permutation.append(i)
			digit = digit + 1
			i = -1
		elif ith == nth:
			permutation.append(i)
	for i in range(10)[::-1]:
		if i not in permutation:
			permutation.append(i)
	return permutation

def solution():
	answer = str()
	lexiPermutationList = lexiPermutation(10 ** 6)
	for i in lexiPermutationList:
		answer = answer + str(i)
	print 'The answer is {}' .format(answer)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
