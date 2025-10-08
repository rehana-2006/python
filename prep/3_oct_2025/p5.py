# An employee gets a monthly salary.
# * If sales ≥ 100 units → bonus = 10%
# * 50–99 units → bonus = 5%
# * <50 → no bonus
# Write a program that asks for salary and sales and prints total salary including bonus.
# Sample Input:
# Enter your salary 40000
# Enter your sales 120
# Sample Output:
# Bonus = 4000
# Total Salary = 44000

s=int(input("Enter your salary:"))
sales=int(input("Enter your sales:"))
if s>0:
    if sales>0 and sales<50:
        print("No bonus")
        print("Total sales:",s)
    elif sales<=99 and sales>=50:
        b=s*5/100
        print("Bouns:",b)
        print("Total sales:",s+b)
    elif sales>=100:
        b=s*10/100
        print("Bouns:",b)
        print("Total sales:",s+b)
    else:
        print ("invalid input")
else:
    print("Invalid input")