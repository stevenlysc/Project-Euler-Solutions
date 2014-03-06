# -*- coding: utf-8 -*-
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

from Utilities import pythagorean_triplet

def main():
    tripletDict = dict()
    for a in xrange(1, 1000):
        for b in xrange(a, 1000 - a):
            for c in xrange(b, 1000 - a - b):
                if pythagorean_triplet(a, b, c):
                    if tripletDict.has_key(a + b + c):
                        tripletDict[a + b + c] += 1
                    else:
                        tripletDict[a + b + c] = 1
    for key in tripletDict:
        if tripletDict[key] == max(tripletDict.values()):
            print key
            break
                        
if __name__ == '__main__':
    main()