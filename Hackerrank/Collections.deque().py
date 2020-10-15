# Perform append, pop, popleft and appendleft methods on an empty deque .

# Input Format

# The first line contains an integer , the number of operations.
# The next  lines contains the space separated names of methods and their values.

# Constraints

# 0 < N <= 100

# Output Format

# Print the space separated elements of deque .

from collections import deque
n = int(input())
d = deque()
for i in range(n):
    e = input().split()
    if e[0] == "append":
        d.append(int(e[1]))
    elif e[0] == "appendleft":
        d.appendleft(int(e[1]))
    elif e[0] == "pop":
        d.pop()
    else:
        d.popleft()
for i in range(len(d)):
    print(d[i], end=" ")