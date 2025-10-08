d=int(input("Enter the distance:"))
if d>=0 and d<=5:
    f=d*10
    if f<50:
        print("the charge is 50")
    else:
        print("the charge is", f)
elif d>=6 and d<=15:
    f=(5*10) + (d-5)*8
    if f<50:
        print ("the charge is 50")
    else:
        print("the charge is ",f)
elif d>15:
    f=(5*10)+(10*8)+(d-15)*6
    if f<50:
        print("the charge is 50")
    else:
        print(" the charge is ",f)
else:
    print("invalid input")