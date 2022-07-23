import math
import os
import random
import re
import sys
# Complete the 'insertionSort2' function below.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
def insertion_sort(l):
    return sorted(l)
if __name__ == '__main__':
    n = int(input().strip())
    ar = [int(i) for i in input().strip().split()]
    arr = insertion_sort(ar)
    print(" ".join(map(str,arr)))