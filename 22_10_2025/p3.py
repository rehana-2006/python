# 3. Write a Python program to count the number of consonants in a given string.
# Input:
# Hello World
# Output:
# Number of consonants: 7

def num_of_consonants(word):
    count=0
    for i in range(0,len(word),+1):
        if word[i].isalpha() and word[i].lower() not in "aeiou" :
            count=count+1
    print(count)
num_of_consonants("hello world")