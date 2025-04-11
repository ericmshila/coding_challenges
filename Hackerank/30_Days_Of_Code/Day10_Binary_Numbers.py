import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())


def convert_binary(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    else:
        return convert_binary(n//2) + [n%2]

def max_ones(base_two):
    max_count = 0
    current_count = 0 
    for char in base_two:
        if char == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count

base_two = convert_binary(n)
print(max_ones(base_two))