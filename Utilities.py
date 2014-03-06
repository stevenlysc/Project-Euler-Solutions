# -*- coding: utf-8 -*-
'''
Some daily used functions in the mathematical area.
'''

def is_prime(x):
    '''Nomal trial division to testify a prime number'''
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, 1 + int(x ** 0.5)):
            if x % i == 0:
                return False
        return True

def is_prime_Miller():
    '''Miller-Rabin primality test based on Fermat's little theorem'''
    pass

def get_prime_sieve(scope):
    '''Find all prime numbers using Sieve of Eratosthenes Algorithm'''
    if scope == 0 or scope == 1:
        return None
    if scope == 2:
        return [2]
    sieve_array = [1 for i in range(scope)]
    prime_array = list()
    for k in range(1 + int(scope ** 0.5)):
        if k == 0 or k == 1:
            sieve_array[k] = 0
        elif sieve_array[k] == 1:
            for n in range(2, 1 + int(scope/k)):
                if n * k < scope:
                    sieve_array[n * k] = 0
        else:
            pass
    for i in range(scope):
        if sieve_array[i] == 1:
            prime_array.append(i)
    return prime_array

def get_factors(number):
    '''Return a sorted list of all the factors of a number'''
    factor_list = list()
    for i in range(1, 1 + int(number ** 0.5)):
        if number % i == 0:
            factor_list.append(i)
            if number/i == i:
                pass
            else:
                factor_list.append(number/i)
    return sorted(factor_list)

def get_prime_factors(number):
    '''Return a dict of all the prime factors of a numberber'''
    if number == 1:
        return None
    working = 2
    primeFactorsDict = dict()
    while working ** 2 <= number:
        count = 0
        while not number % working:
            count += 1
            number //= working
        else:
            if count:
                primeFactorsDict[working] = count
            working += 1
    else:
        if number > 1:
            primeFactorsDict[number] = 1
        return primeFactorsDict

def get_fibonacci_value(value):
    '''
    Generate a fibonacci list according to the value
    The finbonacci list no larger than the given value
    '''
    first, second = 1, 1
    fibonacci_list = [first, second]
    while second <= value:
        first, second = second, first + second
        fibonacci_list.append(second)
    else:
        fibonacci_list.pop()
    return fibonacci_list

def get_fibonacci_length(length):
    '''Generate a fibonacci list no longer than the given lenth'''
    first, second = 1, 1
    fibonacci_list = [first, second]
    count = 2
    while count < length:
        first, second = second, first + second
        fibonacci_list.append(second)
        count += 1
    return fibonacci_list

def is_palindromic(number):
    '''testify a palindromic number'''
    number_list = list(str(number))
    number_list_reverse = number_list[::-1]
    if number_list == number_list_reverse:
        return True
    else:
        return False

def is_palindromic_base_2(number):
    '''testify a palindromic number in binary'''
    number_base_2 = str(bin(number))
    number_base_2 = number_base_2[2:]
    if number_base_2 == number_base_2[::-1]:
        return True
    else:
        return False

def get_largest_common_multiple(*numList): 
    '''Get the largest common multiple of a set of numbers'''
    storeDict = dict()
    for x in numList:
        workingDict = get_prime_factors(x)
        if not workingDict:
            pass
        else:
            for prime, power in workingDict.items():
                if storeDict.has_key(prime):
                    storeDict[prime] = max(storeDict[prime], workingDict[prime])
                else:
                    storeDict.update({prime : power})
    prod = 1
    for prime, power in storeDict.items():
        prod *= prime ** power
    return prod

def pythagorean_triplet(a, b, c):
    '''testify a^2 + b^2 = c^2'''
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

def factorial(number):
    '''Return n!'''
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def triangle_number(index):
    '''Return the index(th) triangle number'''
    return sum(xrange(1, index + 1))

def collatz_sequence(number):
    '''Return a sequence of numbers of Collatz Problem start from given number'''
    collatz_list = list()
    collatz_list.append(number)
    while number != 1:
        if number % 2 == 0:
                number = number / 2
                collatz_list.append(number)
        else:
            number = 3 * number + 1
            collatz_list.append(number)
    return collatz_list

def latticePath(x):
    '''Lattice Path'''
    lattice_path_list = [range(x + 1) for i in range(x + 1)]

    for row in range(x + 1):
        for line in range(x + 1):
            if row ==0 or line == 0:
                lattice_path_list[row][line] = 1
            else:
                lattice_path_list[row][line] = lattice_path_list[row - 1][line] + lattice_path_list[row][line - 1]

    return lattice_path_list[-1][-1]

def amicable_number(number):
    '''Return all the amicable numbers as a Dict under the given number'''
    amicableDict = dict()
    for i in xrange(2, number + 1):
        factor_list = get_factors(i)
        factor_list.pop()
        temp = sum(factor_list)
        factor_list_tmp = get_factors(temp)
        factor_list_tmp.pop()
        if temp < number and i != temp and i == sum(factor_list_tmp) and temp not in amicableDict.keys():
            amicableDict.update({i : temp})
    return amicableDict

def lexicographic_permutation(nth):
    '''Return the nth lexicographic permutation of the given digits'''
    millionth = 0
    permutation = list()
    i = -1
    digit = 1
    while millionth < nth:
        i += 1
        while i in permutation:
            i += 1
        millionth += factorial(10 - digit)
        if millionth > nth:
            millionth -= factorial(10 - digit)
            permutation.append(i)
            digit += 1
            i = -1
        elif millionth == nth:
            permutation.append(i)
    for i in range(10)[::-1]:
        if i not in permutation:
            permutation.append(i)
    return permutation

def day_of_week(year, month, day):
    '''Return the day of any date'''
    template = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= month - 1
    return (year + year/4 - year/100 + year/400 + template[month - 1] + day) % 7

def curious_number(number):
    '''testify whether one number is a curious number or not'''
    num_str = str(number)
    sum_factorial = 0
    for i in num_str:
        sum_factorial += factorial(int(i))
    if sum_factorial == number:
        return True
    else:
        return False    

def circular_number(number):
    '''Return a number's circular number'''
    cir_list = [number]
    num_str = str(number)
    for i in range(len(num_str)):
        if num_str[i:] + num_str[:i] != num_str:
            cir_list.append(int(num_str[i:] + num_str[:i]))
    return cir_list

if __name__ == '__main__':
    pass
