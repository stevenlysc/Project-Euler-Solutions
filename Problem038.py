#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

import time

def solution():
	numList = list()
	for x in xrange(1, 10000):
		for n in xrange(2, 9 / len(str(x)) + 1):
			tmp = str()
			for i in xrange(n):
				tmp += str(x * (i+ 1))
			if len(tmp) == 9 and len(set(tmp)) == 9 and not '0' in tmp:
				numList.append(int(tmp))
	print 'The answer is {}' .format(max(numList))

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
