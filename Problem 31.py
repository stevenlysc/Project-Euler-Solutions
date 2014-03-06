# -*- coding: utf-8 -*-
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

def main():
    count = 0
    for _100_pence in xrange(3):
        for _50_pence in xrange((200 - _100_pence * 100) / 50 + 1):
            for _20_pence in xrange((200 - _100_pence * 100 - _50_pence * 50) / 20 + 1):
                for _10_pence in xrange((200 - _100_pence * 100 - _50_pence * 50 - _20_pence * 20) / 10 + 1):
                    for _5_pence in xrange((200 - _100_pence * 100 - _50_pence * 50 - _20_pence * 20 - _10_pence * 10) / 5 + 1):
                        for _2_pence in xrange((200 - _100_pence * 100 - _50_pence * 50 - _20_pence * 20 - _10_pence * 10 - _5_pence * 5) / 2 + 1):
                            count += 1
    print count + 1


if __name__ == '__main__':
    main()