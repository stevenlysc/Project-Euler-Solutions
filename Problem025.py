#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

import time

def lenOfNum(n):
	return len(str(n))

def solution():
	fibonacciList = [0, 1, 1]
	while lenOfNum(fibonacciList[:len(fibonacciList)-2:-1][0]) < 1000:
		fibonacciList.append(sum(fibonacciList[:len(fibonacciList)-3:-1]))
	print 'The answer is {}' .format(len(fibonacciList)-1)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()

