#i /usr/bin/python
# -*- coding: utf-8 -*-
'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

import time

def solution():
	answer = 0
	for i in xrange(1, 1001):
		answer += i ** i
	print 'The answer is {}' .format(answer % 10 ** 10)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
