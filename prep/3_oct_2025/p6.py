# Earnings of a Salesperson:
# * 5% commission for sales ≤ ₹5000
# * 10% for sales 5001–10000
# * 15% for sales > 10000
# Input weekly sales of the salesperson and calculate commission.
# Test Cases with their output:
# 7000 -> 700
# 12000 -> 1800
# 11000 -> 1650

n=int(input("Enter the weekly sales of the salesperson:"))
if n>0 and n<=5000:
    print(n,"->",n*5/100)
elif n>=5001 and n<=10000:
    print(n,"->",n*10/100)
elif n>10000:
    print(n,"->",n*15/100)
else:
    print("Invalid input")