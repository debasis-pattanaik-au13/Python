# Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help.

# Letters in some of the SOS messages are altered by cosmic radiation during transmission. 

# Given the signal received by Earth as a string, s, determine how many letters of Sami's

# SOS have been changed by radiation.

# For example, Earth receives SOSTOT. Sami's original message was SOSSOS. Two of the message

# characters were changed in transit.

# Function Description

# Complete the marsExploration function in the editor below. It should return an integer 

# representing the number of letters changed during transmission.

# marsExploration has the following parameter(s):

#     s: the string as received on Earth

# Input Format

# There is one line of input: a single string, S.

# Note: As the original message is just SOS repeated n times, S’s length will be a multiple of 3.

# Constraints

# 1<=|S|<=99
# S will contain only upper case English letters.

# Output Format

# Print the number of letters in Sami’s message that were altered by cosmic radiation.

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    m = len(s)//3
    char = "SOS" * m
    count = 0
    for i in range(len(s)):
        if s[i] != char[i]:
            count += 1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
