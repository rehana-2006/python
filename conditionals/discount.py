A=int(input("Enter the amount:"))
if A>=1000:
    B=A*10/100
    c=A-B
    print("The final amount :",c)
elif A<1000 and A>=500:
    B=A*5/100
    c=A-B
    print("The final amount :",c)
elif A<500:
    print("The final amount:",A)
    print("No discount")