
""" I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too."""



def array_plus_array(arr1,arr2):
    sum = arr_total(arr1) + arr_total(arr2)
    return sum

def arr_total(arr):
    total = 0
    for i in arr:
        total += i
    return total