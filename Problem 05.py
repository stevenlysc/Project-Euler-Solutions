# -*- coding: utf-8 -*-
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from Utilities import get_largest_common_multiple as get_lcm

def main():
    print get_lcm(*range(1, 21))

if __name__ == '__main__':
    main()