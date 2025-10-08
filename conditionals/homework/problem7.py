age=int(input("Enter your age:"))
if age>0 and age<5:
    print("free")
elif age>=5 and age<=12:
    print("10")
elif age>=13 and age<=64:
    print("20")
elif age>=65:
    print("15")
else:
    print("invalid age")