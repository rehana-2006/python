# 4.  Write a Python program to remove all spaces from a given string.
# Input:
# Python is awesome
# Output:
# Pythonisawesome

def remove_space(word):
    res=word.split()
    result="".join(res)
    print(result)
remove_space("hello world")