# -*- coding: utf-8 -*-
'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def main():
    resPrimeList = [13, 11, 7, 5, 3, 2, 1]
    index        = [i < 100 and '0' + str(i) or str(i) for i in xrange(17, 1000, 17)]
    for num in resPrimeList:
        tempList = list()
        for presence in (i < 100 and '0' + str(i) or str(i) for i in xrange(num, 1000, num)):
            for segment in index:
                if presence[-2:] == segment[:2] and len(presence[0] + segment) == len(set(presence[0] + segment)):
                    tempList.append(presence[0] + segment)
        index = tempList
    ssdSum = 0
    for n in index:
        if n[0] != "0":
            ssdSum += int(n)
    print ssdSum

if __name__ == '__main__':
    main()
