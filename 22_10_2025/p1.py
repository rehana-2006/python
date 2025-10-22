# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.
# You must:
# - Solve it using an inbuilt function (split()).
# - Solve it without using any inbuilt split functions — by using loops and conditions.
# Given:
# sentence = "Emma-is-a-data-scientist"
# Expected Output:
# Emma
# is
# a
# data
# scientist


# 1st answer

def split_the_string(sentence):
    res=sentence.split("-")
    for i in range(0,len(res),+1):
        print(res[i])

split_the_string("Emma-is-a-data-scientist")

#2nd answer

def split_the_string(sentence):
    word=""
    for i in range (0,len(sentence),+1):
        if sentence[i] != "-":
            word=word+sentence[i]
        else:
            print(word)
            word=""
    print(word)
split_the_string("Emma-is-a-data-scientist")
