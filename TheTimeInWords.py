#!/bin/python3
#hackerrank.com

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    number = {0: " o' clock", 
            1: "one", 
            2: "two", 
            3: "three", 
            4: "four", 
            5: "five", 
            6: "six", 
            7: "seven", 
            8: "eight", 
            9: "nine", 
            10: "ten", 
            11: "eleven", 
            12: "twelve", 
            13: "thirteen", 
            14: "fourteen", 
            15: "quarter", 
            16: "sixteen", 
            17: "seventeen", 
            18: "eighteen", 
            19: "nineteen", 
            20: "twenty", 
            21: "twenty one", 
            22: "twenty two", 
            23: "twenty three", 
            24: "twenty four", 
            25: "twenty five", 
            26: "twenty six", 
            27: "twenty seven", 
            28: "twenty eight", 
            29: "twenty nine", 
            30: "half"}

    if m == 0:return number[h] + number[0]
    if m == 15: return number[m] + " past " + number[h]
    if m < 9: return number[m] + " minute past " + number[h]
    if m < 30: return number[m] + " minutes past " + number[h]
    if m == 30: return number[m] + " past " + number[h]
    if m == 45: return number[60 - m] + " to " + number[h + 1]
    if m < 60: return number[60 - m] + " minutes to " + number[h + 1]
    if m == 15: return number[m] + " past " + number[h]
    if m == 1: return number[m] + " minute past " + number[h]
    if m >30: return number[m] + " minutes past " + number[h]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
