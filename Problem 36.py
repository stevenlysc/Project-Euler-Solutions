# -*- coding: utf-8 -*-
'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

from Utilities import is_palindromic, is_palindromic_base_2

def main():
    pali_list = list()
    for i in xrange(1, 10 ** 6 + 1):
        if is_palindromic(i) and is_palindromic_base_2(i):
            pali_list.append(i)
    print sum(pali_list)

if __name__ == '__main__':
    main()