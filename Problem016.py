#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import time

def solution():
	tmp = 2 ** 1000
	tmpStr = str(tmp)
	answer = 0
	for i in xrange(len(tmpStr)):
		answer = answer + int(tmpStr[i])
	print 'The answer is {}' .format(answer)
	return

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))
	return


if __name__ == '__main__':
	main()
