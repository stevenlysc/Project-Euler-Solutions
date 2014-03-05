# -*- coding: utf-8 -*-
'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''

from urllib import urlopen
import re

rawTri   = urlopen('http://projecteuler.net/project/triangle.txt').read()
link     = re.compile(' 0')
rawTri   = re.sub(link, ' ', rawTri)
link     = re.compile('\n0')
rawTri   = re.sub(link, '\n', rawTri)
triangle = [[int(i) for i in x.split(' ')] for x in rawTri.split('\n')[:-1]]

def main():
    for row in xrange(len(triangle) - 1):
        for column in xrange(len(triangle[row + 1])):
            if column == 0:
                triangle[row + 1][column] += triangle[row][column]
            elif column == len(triangle[row + 1]) - 1:
                triangle[row + 1][column] += triangle[row][column - 1]
            else:
                triangle[row + 1][column] += max(triangle[row][column], triangle[row][column - 1])

    print max(triangle[-1])

if __name__ == '__main__':
    main()