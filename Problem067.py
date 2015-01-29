#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''

import urllib
import time

def inputPrep(url):
	arg = urllib.urlopen(url).read().split()
	inputList = [[] for i in xrange(100)]
	for r in xrange(100):
		for c in xrange(r+1):
			if arg[(1+r)*r/2 + c][:1] == '0':
				inputList[r].append(int(arg[(1+r)*r/2 + c][1:]))
			else:
				inputList[r].append(int(arg[(1+r)*r/2 + c]))
	return inputList

def solution(inList):
	for r in xrange(1, 100):
		for c in xrange(r+1):
			if c == 0:
				inList[r][c] += inList[r-1][c]
			elif c == r:
				inList[r][c] += inList[r-1][c-1]
			else:
				inList[r][c] += max([inList[r-1][c-1], inList[r-1][c]])
	print 'The answer is {}' .format(max(inList[99]))

def main():
	url = 'https://projecteuler.net/project/resources/p067_triangle.txt'
	inList = inputPrep(url)
	start = time.clock()
	solution(inList)
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
