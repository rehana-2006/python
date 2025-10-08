x=int(input("Enter the x:"))
y=int(input("Enter the y:"))
if x>0 and y>0:
    print("Quadrant 1")
elif x<0 and y>0:
    print("Quadrant 2")
elif x<0 and y<0:
    print("Quadrant 3")
elif x>0 and y<0:
    print("Quadrant 4")
#else:
elif x==0 and y==0:
    print("Center")

#quadrant of a point