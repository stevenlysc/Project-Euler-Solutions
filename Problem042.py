#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

import time, urllib

def inputPrep(url):
	return urllib.urlopen(url).read().replace('"', '').split(',')

def wordValue(word):
	value = 0
	for i in word:
		value += ord(i) - ord('A') + 1
	return value
	      
def solution():
	url = 'https://projecteuler.net/project/resources/p042_words.txt'
	triList = [i * (i + 1) / 2 for i in xrange(1, 20)]
	inList = inputPrep(url)
	answer = 0
	for word in inList:
		if wordValue(word) in triList:
			answer += 1
	print 'The answer is {}' .format(answer)

def main():
	start = time.clock()
	solution()
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
