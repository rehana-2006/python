# 2. Write a Python program to reverse a given string in two ways:
# - Using an inbuilt function or slicing
# - Without using any inbuilt functions/Slicing
# Given:
# str1 = "Python"
# Expected Output:
# nohtyP

#1st answer

def reverse_string(word):
    print(word[::-1])
reverse_string("Python")

# 2nd answer

def reverse_string(word):
    res=""
    i=len(word)-1
    while i>=0:
        res=res+word[i]
        i=i-1
    print(res)
reverse_string("Python")