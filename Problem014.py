#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import time

def collaztSeq(n):
	return n / 2 if n % 2 == 0 else 3 * n + 1

def lenCollatzSeq(interDict, num):
	length = 1
	n = num
	while n != 1:
		n = collaztSeq(n)
		if interDict.has_key(n):
			length = length + interDict[n]
			interDict[num] = length
			return length
		else:
			length = length + 1
	interDict[num] = length
	return length

def solution():
	answer = 0
	maxLen = 0
	interDict = {}
	for i in xrange(1, 10 ** 6 + 1):
		tmpLen = lenCollatzSeq(interDict, i)
		if tmpLen > maxLen:
			maxLen = tmpLen
			answer = i
	print 'The answer is {}' .format(answer)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
