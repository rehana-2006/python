#assignment operator
x=5
y=2
print(x>y)
print(x<y)
print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)


#to find a number even  or odd
#step 1: getting the input the user
#n=int(input("Enter a number:"))
#print(n)
#step 2:condition check
#if n%2==0:
 #   print("The number is even")
#else:
    #print("The number is odd")


n=int(input("Enter a number:"))
if (n%3==0 or n%5==0):
    print("divisible")
else:
    print("not divisible")