# Print the below pattern if n = 3
# 1 1 1
# 2 2 2
# 3 3 3


def number_pattern(n:int):
    res=""
    for i in range(1,n+1):
        for j in range(1,n+1):
            res+=str(i)
        if len(res)==n:
            print(res)
            res=""
number_pattern(4)