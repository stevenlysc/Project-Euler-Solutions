# -*- coding: utf-8 -*-
'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def denominator(x):
    return set(range(x / 10 + 10, 100, 10) + range(x / 10 * 10 + 1, x / 10 * 10 + 10) + range(x % 10 + 10, 100, 10) + range(x % 10 * 10 + 1, x % 10 * 10 + 10))

def GCD(i, j):
    '''Greatest Common Divisor'''
    if j > i:
        i, j = j, i
    while 1:
        i, j = j, i % j
        if j == 0:
            break
    return i

def main():
    product_i = 1
    product_j = 1
    for i in xrange(11, 100):
        if i % 10 == 0:
            continue
        else:
            for j in denominator(i):
                if j > i:
                    if i / 10 == j / 10 and float(i % 10) / (j % 10) == float(i) / j:
                        product_j *= j
                        product_i *= i
                    elif i / 10 == j % 10 and float(i % 10) / (j / 10) == float(i) / j:
                        product_j *= j
                        product_i *= i
                    elif i % 10 == j / 10 and float(i / 10) / (j % 10) == float(i) / j:
                        product_j *= j
                        product_i *= i
                    elif i % 10 == j % 10 and float(i / 10) / (j / 10) == float(i) / j:
                        product_j *= j
                        product_i *= i
                    else:
                        pass
    print product_j / GCD(product_i, product_j)

if __name__ == '__main__':
    main()
