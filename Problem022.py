#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import urllib, time

def inputPrep(url):
	return sorted(urllib.urlopen(url).read().replace('"', '').split(','))

def nameScore(name):
	score = 0
	for i in name:
		score += ord(i) - 64
	return score

def solution(nameList):
	totalScore = 0
	for index in xrange(len(nameList)):
		totalScore += (index + 1) * nameScore(nameList[index])
	print 'The answer is {}' .format(totalScore)

def main():
	url = 'https://projecteuler.net/project/resources/p022_names.txt'
	nameList = inputPrep(url)
	start = time.clock()
	solution(nameList)
	print 'Elapsed: {} ms' .format(1000 * (time.clock() - start))


if __name__ == '__main__':
	main()
