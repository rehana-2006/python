n=int(input("enter a two digit number"))
a=n//10 #tenth digit
b=n%10 #ones digit
m=a+b
j=a*b
if (m+j)==n:
    print("great")
else:
    print("no")