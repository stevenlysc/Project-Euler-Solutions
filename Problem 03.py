# -*- coding: utf-8 -*-
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from Utilities import get_prime_factors

def main():  
    target_num= 600851475143
    prime_factor_list = get_prime_factors(target_num).keys()
    largest_prime_factor = max(prime_factor_list)
    print largest_prime_factor

if __name__ == '__main__':
    main()