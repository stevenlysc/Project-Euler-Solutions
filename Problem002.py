#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

import time

def solution():
    first, second = 1, 2
    fibList = [first, second]
    evenSum = second
    
    while second < 4000000:
        first, second = second, first + second
        fibList.append(second)
        if second % 2 == 0 and second < 4000000:
            evenSum = evenSum + second
   
    print 'The answer is {}' .format(evenSum)
    return

def main():
    start = time.clock()
    solution()
    print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))

if __name__ == '__main__':
    main()
