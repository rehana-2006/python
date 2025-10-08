x=5
y=10
print(x,y)
x=x+y
y=x-y
x=x-y
print(x,y)

x,y=y,x
print(x,y)

temp=x
x=y
y=temp
print(x,y)