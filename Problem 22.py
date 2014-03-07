# -*- coding: utf-8 -*-
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import urllib
import re

def order_worth(name):
    worth = 0
    for i in name:
        worth += ord(i) - 64
    return worth

def main():
    names = urllib.urlopen('http://projecteuler.net/project/names.txt').read()
    r = re.compile(r'"(.+?)"')
    result = re.findall(r, names)
    result = sorted(result)
    
    name_score = 0
    for i in xrange(len(result)):
        name_score += (i + 1) * order_worth(result[i])
    
    print name_score

if __name__ == '__main__':
    main()