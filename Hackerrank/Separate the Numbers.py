# A numeric string, s, is beautiful if it can be split into a sequence of two or more positive integers, a1,a2,….. ,
# an, satisfying the following conditions:

# ai-ai-1 = 1 for any 1≤ i≤ n (i.e., each element in the sequence is 1 more than the previous element).
# No ai contains a leading zero. For example, we can split s = 10203 into {1, 02, 03 } the sequence ,
# but it is not beautiful because 02 and 03 have leading zeroes.
# The contents of the sequence cannot be rearranged. For example, we can split s = 312 into the 
# sequence {3, 1, 2}, but it is not beautiful because it breaks our first constraint (i.e., 1–3 ≠ 1 ).
# You must perform q queries, where each query consists of some s string . For each query, print 
# whether or not the string is beautiful on a new line. If it’s beautiful, print YES x, where x is the
# first number of the increasing sequence (if there are multiple such values of x , 
# choose the smallest); otherwise, print NO instead.

# Input Format

# The first line contains an integer denoting q (the number of strings to evaluate).
# Each of the q subsequent lines contains some s string for a query.

# Constraints
# 1 ≤ q ≤ 10
# 1 ≤ |s| ≤ 32
# Each character in s is a decimal digit from 0 to 9 (inclusive).

# Output Format

# For each query, print its answer on a new line (i.e., either YES x where x is the smallest first number
# of the increasing sequence, or NO).

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    arr = s.split()
    check = True
    for i in range(1, len(s) // 2 + 1):
        n = int(s[:i])
        if ''.join(map(str, [n+j for j in range(len(s)//i)]))[:len(s)] == s:
            print("YES "+ str(n))
            check = False
            break
    if check:            
        print('NO')
        
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)