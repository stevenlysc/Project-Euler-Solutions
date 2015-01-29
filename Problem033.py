#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

import time

def preCheck(x, y):
	if len(set(str(x))) == 1 or len(set(str(y))) == 1:
		return False
	checkSet = set(str(x)[:] + str(y)[:])
	if not '0' in checkSet and len(checkSet) == 3:
		return True
	else:
		return False

def check(a, b):
	digitList = list()
	for i in str(a):
		digitList.append(i)
	for j in str(b):
		if not j in digitList:
			digitList.append(j)
	fraction = 0
	for i in str(a):
		for j in str(b):
			if j == i:
				digitList.remove(j)
				fraction = float(int(digitList[0])) / int(digitList[1])
	if float(a) / b == fraction:
		return True
	else:
		return False

def toLowestCommonTerm(a, b):
	bb = b
	while a != 0:
		a, b = b % a, a
	return bb / b 

def solution():
	prodNumerator, prodDenominator = 1, 1
	for a in xrange(11, 100):
		for b in xrange(a, 100):
			if preCheck(a, b):
				if check(a, b):
					prodNumerator *= a
					prodDenominator *= b
	answer = toLowestCommonTerm(prodNumerator, prodDenominator)
	print 'The answer is {}' .format(answer)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()

