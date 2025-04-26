
"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

"""

ef is_even(i):
    if i % 2 == 0:
        return True
def is_odd(i):
    if i % 2 != 0:
        return True   

def find_outlier(integers):
    odd_numbers = []
    even_numbers = []
    for i in integers: 
        if is_even(i):
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    if len(odd_numbers) == 1 :
        return odd_numbers[0]
    elif len(even_numbers) == 1:
        return even_numbers[0]