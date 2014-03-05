# -*- coding: utf-8 -*-
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from Utilities import is_palindromic

def main():
    palindrome_list = list()

    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindromic(i * j):
                palindrome_list.append(i * j)

    print max(palindrome_list)

if __name__ == '__main__':
    main()