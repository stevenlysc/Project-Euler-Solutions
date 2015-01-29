#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

import time

def solution():
	sumDiag = 1
	for i in xrange(1, 1002, 2):
		if i == 1:
			pass
		else:
			sumDiag = sumDiag + 4 * i ** 2 - 6 * (i -1)
	print 'The answer is {}' .format(sumDiag)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
