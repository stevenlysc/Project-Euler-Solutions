# -*- coding: utf-8 -*-
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def pandigital(x, y, w):
    pandiList = [i for i in str(x)] + [i for i in str(y)] + [i for i in str(w)]
    if sorted(pandiList) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
        return False

def main():
    numList = list()
    for i in xrange(1, 100):
        for j in xrange(i, 2000):
            if i * j > 10 ** 5:
                break
            else:
                if pandigital(i, j, i * j) and not i * j in numList:
                    numList.append(i * j)
    print sum(numList)

if __name__ == '__main__':
    main()

