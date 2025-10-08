# A stadium sells entry passes with the following rules:
# * If age < 12 → Ticket = ₹50
# * If age between 12–59 → Ticket = ₹120
# * If age ≥ 60 → Ticket = ₹80
# Additionally, if the person’s age is a Even number, give a ₹5 discount.
# Get the input from the user and return the final discounted stadium ticket price.
# Sample Input:
# 59
# Sample Output:
# 120


age=int(input("enter the age:"))
if age>0 and age<12:
    if age%2==0:
        print(50-5)
    else:
        print(50)
elif age>=12 and age<=59:
    if age%2==0:
        print(120-5)
    else:
        print(120)
elif age>=60 and age<=100:
    if age%2==0:
        print(80-5)
    else:
        print(80)
else:
    print("Invalid input")