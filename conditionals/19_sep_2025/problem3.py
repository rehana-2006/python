m=input("Enter the consumer type(residential/commercial):")
n=int(input("Enter the units consumed:"))
if m=="residential":
    if n>=0 and n<=100:
        b=n*3
        print("bill=",b)
    elif n>=101 and n<=200:
        b=n*5
        print("bill=",b)
    elif n>200:
        b=n*7
        print("bill=",b)
    else:
        print("invalid unit")
elif m=="commercial":
    if n>=0 and n<=100:
        b=n*5
        print("bill=",b)
    elif n>=101 and n<=200:
        b=n*7
        print("bill=",b)
    elif n>200:
        b=n*10
        print("bill=",b)
    else:
        print("invalid unit")
else:
    print("invalid input")