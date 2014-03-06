# -*- coding: utf-8 -*-
'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from Utilities import curious_number

def main():
    sum_number = 0
    for i in xrange(3, 2177281):
        if curious_number(i):
            print i
            sum_number += i
    print sum_number

if __name__ == '__main__':
    main()