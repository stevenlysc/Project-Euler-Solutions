#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

import time

def solution():
	count = 1
	for _100Pence in xrange(3):
		for _50Pence in xrange((200 - _100Pence * 100) / 50 + 1):
			for _20Pence in xrange((200 - _100Pence * 100 - _50Pence * 50) / 20 + 1):
				for _10Pence in xrange((200 - _100Pence * 100 - _50Pence * 50 - _20Pence * 20) / 10 + 1):
					for _5Pence in xrange((200 - _100Pence * 100 - _50Pence * 50 - _20Pence * 20 - _10Pence * 10) / 5 + 1):
						for _2Pence in xrange((200 - _100Pence * 100 - _50Pence * 50 - _20Pence * 20 - _10Pence * 10 - _5Pence * 5) / 2 + 1):
							count = count + 1
	print 'The answer is {}' .format(count)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
