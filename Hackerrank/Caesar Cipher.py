# Julius Caesar protected his confidential information by encrypting it in a cipher. Caesar’s cipher rotated every letter in a string by a fixed number, K, making it unreadable by his enemies. Given a string, S, and a number, K, encrypt S and print the resulting string.

# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

# Input Format

# The first line contains an integer, N, which is the length of the unencrypted string.
# The second line contains the unencrypted string, S.
# The third line contains the integer encryption key, K, which is the number of letters to rotate.

# Constraints

# 1<=N<=100 0<=K<=100 S is a valid ASCII string and doesn't contain any spaces. Output Format

# For each test case, print the encoded string.

def caesarCipher(s, k):
    e = ""
    for i in s:
        if i.islower():
            e+= chr((ord(i)-97+k)%26+97)
        elif i.isupper():
            e+= chr((ord(i)-65+k)%26+65)
        else:
            e+= i
    return e