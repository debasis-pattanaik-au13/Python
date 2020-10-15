# Steve wants to reduce s as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Steve out by finding and printing s‘s non-reducible form!

# Note: If the final string is empty, print Empty String.

# Input Format:- A single string, s.

# Constraints
# 1<=n<=100

# Output Format:- If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

def superReducedString(s):
    lst = []
    for i in s:
        if i not in lst:
            lst.append(i)
        
        elif lst[-1] == i:
            lst.pop()

        else:
            lst.append(i)
                
    if len(lst) == 0:
        return "Empty String"
    else:
        return "".join(lst)

