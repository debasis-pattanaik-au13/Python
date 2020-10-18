# In this challenge, you will determine whether a string is funny or not. To determine whether a string 

# is funny, create a copy of the string in reverse e.g. abc -> cba.

# Iterating through each string, compare the absolute difference in the ascii values of the characters 

# at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same 

# for both strings, they are funny.

# Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

# Function Description

# Complete the funnyString function in the editor below. For each test case, it should return a string, either Funny or Not Funny.

# funnyString has the following parameter(s):

#     s: a string to test

# Input Format

# First line of the input will contain an integer T. T testcases follow. 

# Each of the next T lines contains one string S.

# Constraints

# 1 ≤ q ≤ 10

# 2 ≤ length of S ≤ 10000

# Output Format

# For each string, print Funny or Not Funny in separate lines.

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    for _ in range(q):
        st=[str(x) for x in s]
        diff=[abs(ord(a)-ord(b)) for a,b in zip(st,st[1:])]
    if diff == diff[::-1]:
        return "Funny"
    return "Not Funny"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
