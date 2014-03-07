# -*- coding: utf-8 -*-
'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def num_digits(x):
    digits_set = set()
    for i in str(x):
        digits_set.add(i)
    return digits_set


def main():
    for i in set(range(1000, 1668) + range(10000, 16668) + range(100000, 166668)):
        if num_digits(i) == num_digits(2 * i) and num_digits(2 * i) == num_digits(3 * i) \
        and num_digits(3 * i) == num_digits(4 * i) and num_digits(4 * i) == num_digits(5 * i) \
        and num_digits(5 * i) == num_digits(6 * i):
            print i
            break

if __name__ == '__main__':
    main()