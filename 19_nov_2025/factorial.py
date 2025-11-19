# Find the factorials of each of the integers given in an List.

def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

def factorial(nums):
    result=[]
    for el in nums:
       result.append(fact(el))
    return result 

print(factorial([3,4,5]))