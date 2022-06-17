#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    x = 0
    y = 0
    z = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:

            x = x+1
        elif arr[i] < 0:
            y = y+1
        else:
            z = z+1
        # return x,y,z
    p = x/len(arr)
    q = y/len(arr)
    s = z/len(arr)
    print(p)
    print(q)
    print(s)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
