# Amanda has a string of lowercase letters that she wants to copy to a new string. She can 

# perform the following operations with the given costs. She can perform them any number 

# of times to construct a new string :

#     Append a character to the end of string "p" at a cost of 1 dollar. 

#     Choose any substring of "p" and append it to the end of "p" at no charge.

# Given "n" strings s[i], find and print the minimum cost of copying each s[i] to p[i] on a new line.

# Function Description

# Complete the stringConstruction function in the editor below. It should return the minimum cost of copying a string.

# stringConstruction has the following parameter(s): 

#     s: a string 

# Input condition

# The first line contains a single integer, n, denoting the number of strings.

# Each line i of the n subsequent lines contains a single string, si.

# Limitation
# 1<=n<=5
# 1<=m<=105

# Subtasks
# 1<=m<=103 for 45% of the maximum score.

# Output condition

# For each string (where 0<=i<=n), print the minimum cost of constructing string on a new line.

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    return(len(set(s)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
