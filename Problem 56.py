# -*- coding: utf-8 -*-
'''
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''

def digital_sum(number):
    dig_sum = 0
    for i in str(number):
        dig_sum += int(i)
    return dig_sum

def main():
    max_dig_sum = 0
    for a in xrange(1, 101):
        for b in xrange(1, a + 1):
            dig_sum = digital_sum(a ** b)
            if dig_sum > max_dig_sum:
                max_dig_sum = dig_sum
    print max_dig_sum
    
if __name__ == '__main__':
    main()