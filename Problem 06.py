# -*- coding: utf-8 -*-
'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def main():
    sum_of_squares = sum([i ** 2 for i in range(1, 101)])
    square_of_sum = sum(range(1, 101)) ** 2
    print square_of_sum - sum_of_squares

if __name__ == '__main__':
    main()