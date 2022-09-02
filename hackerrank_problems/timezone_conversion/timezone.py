#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    time = int(s[0:2])

    if time == 12 and s[8:len(s)] == "AM":
        return ("00"+s[2:len(s)-2])
    elif time == 12 and s[8:len(s)] == "PM":
        return (s[0:len(s)-2])
    elif s[8:len(s)] == "PM":
        return (str(time+12)+s[2:len(s)-2])
    elif s[8:len(s)] == "PM" and time == 12:
        return (s[0:len(s)-2])
    else:
        return (s[0:len(s)-2])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
