# Given integer n print its first 10 multiples


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())


for i in range(1,11):
    print(f"{n} x {i} = {n*i}" )
