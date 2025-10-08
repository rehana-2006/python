# A cinema charges:
# * ₹150 for ages under 18
# * ₹250 for ages 18–60
# * ₹100 for ages above 60
# Write a program that asks for age and prints the ticket price.
# Sample Input:
# 65
# Sample Output:
# 100


age=int(input("Enter the age:"))
if  age>0 and age<18:
    print("150")
elif age>=18 and age<=60:
    print("250")
elif age>60 and age<100:
    print("100")
else:
    print("Invalid input")