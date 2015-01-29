#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import time

def dayOfWeek(year, month, day):
	# return the day of any date
	template = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	if month < 3:
		year -= month - 1
	return (year + year/4 - year/100 + year/400 + template[month-1] + day) % 7

def solution():
	answer = 0
	for year in xrange(1901, 2001):
		for month in xrange(1, 13):
			if not dayOfWeek(year, month, 1):
				answer += 1
	print 'The answer is {}' .format(answer)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
