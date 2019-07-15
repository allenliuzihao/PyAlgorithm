'''
File contains O(n^2) and O(nlogn) solution for interger multiplication
'''

import math


# Given two array [2, 3, 4] and [1, 2, 3]
# 	  return [3, 5, 7]

def addNumber(a, b):
    result = []
    longer_digits = a if len(a) > len(b) else b
    shorter_digits = a if longer_digits != a else b
    while len(shorter_digits) != len(longer_digits):
        shorter_digits.insert(0, 0)
    over_flow = 0
    for i in xrange(1, len(longer_digits) + 1):
        result.append((shorter_digits[-i] + longer_digits[-i] + over_flow) % 10)
        over_flow = (shorter_digits[-i] + longer_digits[-i] + over_flow) / 10
    if over_flow != 0:
        result.append(over_flow)
    return result[::-1]


# Naive implementation for the integer multiplication
# Same as grade school mutiplication method
# Runs in O(n^2)

def naive_multiply(a, b):
    if a == 0 or b == 0:
        return 0
    elif a == 1 or b == 1:
        return a if a != 1 else b
    else:
        a_digits = []
        b_digits = []
        while a:
            digit = a % 10
            a = a / 10
            a_digits.append(digit)
        while b:
            digit = b % 10
            b = b / 10
            b_digits.append(digit)
        a_digits = a_digits[::-1]
        b_digits = b_digits[::-1]
        longer_digits = a_digits if len(a_digits) > len(b_digits) else b_digits
        shorter_digits = a_digits if longer_digits != a_digits else b_digits
        before_addition = []
        index_shorter = 0
        for i in reversed(shorter_digits):
            curr_addition = []
            digits_for_next = 0
            for j in reversed(longer_digits):
                    curr_addition.insert(0, (i * j + digits_for_next) % 10)
                    digits_for_next = 0 if (i * j + digits_for_next) / 10 == 0 else (i * j + digits_for_next) / 10
            if digits_for_next != 0:
                curr_addition.insert(0, digits_for_next)
            curr_addition += [0] * index_shorter
            before_addition.append(curr_addition)
            index_shorter += 1
        index = 1
        curr_addition = before_addition[0]
        while index < len(before_addition):
            curr_addition = addNumber(curr_addition, before_addition[index])
            index += 1
        return int(''.join(map(str, curr_addition)))


#
#   Given a list of digits of the form [0, 0, 1, 0]
#   Return [1, 0]
#

def preprocess_digits(digits):
    process = digits[:]
    hasNotZero = False
    for i in digits:
        if i != 0:
            hasNotZero = True
    if hasNotZero:
        while process[0] == 0:
            process.remove(0)
        return process
    else:
        return [0]


# Divide and Conquer implementation of the multiplication algorithm of two numbers of
# even and same number of digits
# Run in O(n^1.59) time
# 
# Note that this algorithm doesn't check the overflow. Don't let the a or b to be too
# large

def integer_multiply(a, b):
    if a / 10 == 0 or b / 10 == 0 or len(str(a)) != len(str(b)) or len(str(a)) % 2 == 1:
        return a * b
    else:
        a_digits = []
        b_digits = []
        while a:
            digit = a % 10
            a = a / 10
            a_digits.insert(0, digit)
        while b:
            digit = b % 10
            b = b / 10
            b_digits.insert(0, digit)
        a = int(''.join(map(str, a_digits[0:len(a_digits) / 2])))
        b_preprocess = preprocess_digits(a_digits[len(a_digits) / 2:])
        b = int(''.join(map(str, b_preprocess)))
        c = int(''.join(map(str, b_digits[0:len(b_digits) / 2])))
        d_preprocess = preprocess_digits(b_digits[len(b_digits) / 2:])
        d = int(''.join(map(str, d_preprocess)))
        #print "a: ", a, " b: ", b, " c: ", c, " d: ", d
        ac = integer_multiply(a, c)
        bd = integer_multiply(b, d)
        #print "ac: ", ac, " bd: ", bd
        a_plus_bc_plus_d = integer_multiply(a + b, c + d)
        ad_plus_bc = a_plus_bc_plus_d - (ac + bd)
        return pow(10, len(a_digits)) * ac + ad_plus_bc * pow(10, math.ceil(float(len(a_digits) / 2))) + bd

if __name__ == '__main__':
#   for i in xrange(0, 999):
#		for j in xrange(0, 999):
#			if i * j != naive_multiply(i, j):
#			    print i, " ", j
    print integer_multiply(123, 468) == 123 * 468
    #print integer_multiply(1220, 4640) == 1220 * 4640