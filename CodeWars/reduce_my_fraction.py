"""
Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language) of strictly positive integers, and the reduced fraction must be returned as an array/tuple:

input:   [numerator, denominator]
output:  [reduced numerator, reduced denominator]
example: [45, 120] --> [3, 8]
All numerators and denominators will be positive integers.

Note: This is an introductory Kata for a series... coming soon!
"""
import math
def reduce_fraction(fraction):
    a = fraction[0] #45
    b = fraction[1] # 120
    gcd = math.gcd(a,b)
    # divde each part of fraction by the gcd 
    result = (a//gcd, b//gcd)
    return result