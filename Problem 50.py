# -*- coding: utf-8 -*-
'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from Utilities import get_prime_sieve, get_prime_truthtable

def main():
    prime_list = get_prime_sieve(5 * 10 ** 5)
    prime_truthtable = get_prime_truthtable(10 ** 6)
    #print len(prime_list) 41538
    count = 0
    total = 0
    for i in xrange(len(prime_list) - 2):
        tem_count = 1
        tem_total = prime_list[i]
        #print tem_total, prime_truthtable[tem_total], '\n'
        while tem_total < 10 ** 6:
            #print tem_total, 'with i =', i
            i += 1
            tem_total += prime_list[i]
            tem_count += 1
        tem_total = tem_total - prime_list[i]
        if prime_truthtable[tem_total] and tem_count > count:
            count = tem_count
            total = tem_total
            #print total, 'and', count
    print total


if __name__ == '__main__':
    main()