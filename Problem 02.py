# -*- coding: utf-8 -*-
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

from Utilities import get_fibonacci_value

def main():
    value = 4 * 10 ** 6
    fibonacci_list = get_fibonacci_value(value)
    sum_even = 0
    for i in fibonacci_list:
        if not i % 2:
            sum_even += i
    print sum_even


if __name__ == '__main__':
    main()