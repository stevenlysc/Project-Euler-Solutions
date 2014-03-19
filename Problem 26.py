# -*- coding: utf-8 -*-
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

def recur_circle(x):
    number = 1
    divide_list = list()
    count = 0
    while 1:
        if number < x:
            number *= 10
        else:
            number %= x
            if number == 0:
                return 0
            if not number in divide_list:
                divide_list.append(number)
                count += 1
            else:
                break
    return count

def main():
    val = 0
    d_val = 0
    for d in xrange(2, 1000):
        temp = recur_circle(d)
        if temp > val:
            val = temp
            d_val = d
    print d_val
    
if __name__ == '__main__':
    main()