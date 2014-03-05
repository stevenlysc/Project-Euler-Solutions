# -*- coding: utf-8 -*-
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

def main():
    numDict = {1: 'one', 2: 'tow', 3: 'three', 4: 'four', 5: 'five', \
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
                19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
                50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
                90: 'ninety'}
    num_letter_10 = 0
    num_letter_20 = 0
    for i in xrange(1, 10):
        num_letter_10 += len(numDict[i])
    for i in xrange(1, 20):
        num_letter_20 += len(numDict[i])
    num_letter_100 = num_letter_20 + 10 * (len(numDict[20]) + len(numDict[30]) \
        + len(numDict[40]) + len(numDict[50]) + len(numDict[60]) + len(numDict[70])\
         + len(numDict[80]) + len(numDict[90])) + 8 * num_letter_10
    num_letter_1000 = 9 * len('hundred') + 891 * len('hundredand') + 100 * num_letter_10 + 10 * num_letter_100 + len('onethousand')

    print num_letter_1000

if __name__ == '__main__':
    main()