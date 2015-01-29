#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import time

def solution():
	periDict = dict()
	for a in xrange(1, 334):
		for b in xrange(a, 500):
			for c in xrange(b, 1000 - a - b):
				if a * a + b * b == c * c:
					if periDict.has_key(a + b + c):
						periDict[a + b + c] += 1
					else:
						periDict[a + b + c] = 1
	for key in periDict.keys():
		if periDict[key] == max(periDict.values()):
			print 'The answer is {}' .format(key)
			break

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
