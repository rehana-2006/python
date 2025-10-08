a=int(input("enter a side:"))
b=int(input("enter a side:"))
c=int(input("enter a side:"))
if (a+b<=c) or (b+c<=c) or (a+c<=c):
    print("not a valid triangle")
elif a==b==c:
    print("Equilateral triangle")
elif a==b or b==c or a==c :
    print("Isosceles triangle")
else:
    print("Scalene triangle")


