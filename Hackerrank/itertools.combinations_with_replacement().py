# You are given a string S.
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.


# Input Format :
# A single line containing the string S and integer value k separated by a space.

# Constraints :

#     0 < k <= len(s)
#     The string contains only UPPERCASE characters.


# Output Format :
# Print the combinations with their replacements of string S on separate lines. 

from itertools import combinations_with_replacement
string = input().split()
string[0] = sorted(string[0])
k = list(combinations_with_replacement(string[0], int(string[1])))
for i in range(len(k)):
    print(''.join(k[i]))