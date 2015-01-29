#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import time

def isPalindromic(number, base):
	reverse = 0
	k = number
	while k > 0:
		reverse = base * reverse + k % base
		k = k / base
	return reverse == number

def solution():
	total = 0
	for i in xrange(1, 10 ** 6):
		if isPalindromic(i, 10) and isPalindromic(i, 2):
			total += i
	print 'The answer is {}' .format(total)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
