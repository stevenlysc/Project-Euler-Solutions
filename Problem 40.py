# -*- coding: utf-8 -*-
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

def main():
    num_str = str()
    for i in xrange(1, 200001):
        num_str += str(i)
    print int(num_str[0]) * int(num_str[9]) * int(num_str[99]) * int(num_str[999]) * int(num_str[9999]) * int(num_str[99999]) * int(num_str[999999])



if __name__ == '__main__':
    main()