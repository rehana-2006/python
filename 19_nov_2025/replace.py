# Perform search and replace without using library functions. Given a String "This is programming" find_str = "is" and
#  replace "are" result should be "There are programming"

def replace(s,find,replace):
    result=""
    new=""
    for i in s:
        if i != " ":
            result+=i
        else:
            if result!=find:
                new+=result+" "
                result=""
            else:
                result=replace
                new+=result+" "
                result=""
    new+=result
    print(new)


replace("This nara programming","nara","narayanan")