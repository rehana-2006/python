#find the character is vowel or not
c=input("enter the character:")
match c:
    case "a"|"e"|"i"|"o"|"u":
        print("it is vowel")
    case _:
        print("it is consonant")