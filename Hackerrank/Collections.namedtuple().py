# Dr. John Wesley has a spreadsheet containing a list of student's IDs, Marks, class and name.
# Your task is to help Dr. Wesley calculate the average marks of the students.

# Collections.namedtuple() in Python - Hacker Rank Solution

# Note:
# 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)


# Input Format :
# The first line contains an integer N, the total number of students.
# The second line contains the names of the columns in any order.
# The next N lines contains the marks, IDs, name and class, under their respective column names.

# Constraints :

#     0 <= N <= 100


# Output Format :
# Print the average marks of the list corrected to 2 decimal places.

from collections import namedtuple
n = int(input())
a = input()
average = 0
Student = namedtuple('Student', a)
for i in range(n):
    student = Student(*input().split())
    average += int(student.MARKS)
print(average/n)