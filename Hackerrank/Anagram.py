# Two words are anagrams of one another if their letters can be rearranged to form the other word.

# In this challenge, you will be given a string. You must split it into two contiguous substrings,

# then determine the minimum number of characters to change to make the two substrings into anagrams of one another.

# For example, given the string 'abccde', you would break it into two parts: 'abc' and 'cde'. 

# Note that all letters have been used, the substrings are contiguous and their lengths are equal. 

# Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. 

# Two changes were necessary.

# Function Description

# Complete the anagram function in the editor below. It should return the minimum number of characters to 

# change to make the words anagrams, or -1 if it's not possible.

# anagram has the following parameter(s):

#     s: a string

# Input Format:-

# The first line will contain an integer, T, representing the number of test cases. 

# Each test case will contain a string having length len(S1)+len(S2), which will be 

# the concatenation of both the strings described above in the problem.The given string

# will contain characters from a to z.

# Constraints:-

# 1<=T<=100
# 1<=len(S1)+len(S2)<=104

# Output Format:-

# An integer corresponding to each test case is printed in a different line, i.e. 

# the number of changes required for each test case. Print -1 if it is not possible.

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    s1 = list(s[:len(s)//2])
    s2 = list(s[len(s)//2:])
    count = 0
    if len(s) % 2 != 0:
        return -1
    for char in s1:
        if char in s2:
            s2.remove(char)
        else:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
