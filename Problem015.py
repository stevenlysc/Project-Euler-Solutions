#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
https://projecteuler.net/problem=15
'''

import time
import math

def solution():
	latticeList = [[1] for i in xrange(21)]
	latticeList[0] = [1 for i in xrange(21)] 
	for row in xrange(1, 21):
		for col in xrange(1, 21):
			latticeList[row].append(latticeList[row][col-1] + latticeList[row-1][col])
	print 'The answer is {}' .format(latticeList[20][20])

def solution_math():
	print math.factorial(40) // (math.factorial(20) * math.factorial(20))

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
