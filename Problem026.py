#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

import time

def lenRecurCycle(n):
	number, count = 1, 0
	divideList = list()
	while True:
		if number < n:
			number = number * 10
		else:
			number = number % n
			if number == 0:
				return 0
			if not number in divideList:
				divideList.append(number)
				count = count + 1
			else:
				break
	return count

def solution():
	lenRecur, dValue = 0, 0
	for d in xrange(1, 1001):
		tmp = lenRecurCycle(d)
		if lenRecur < tmp:
			lenRecur = tmp
			dValue = d
	print 'The answer is {}' .format(dValue)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
