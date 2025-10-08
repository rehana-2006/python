# Lily is N years old.
# On every odd birthday (1, 3, 5, …) → she gets 1 toy.
# On every even birthday (2, 4, 6, …) → she gets money.
# The money starts at ₹10 on her 2nd birthday.
# On each next even birthday, it increases by ₹10 more:
# 2nd birthday → ₹10
# 4th birthday → ₹20
# 6th birthday → ₹30
# and so on.
# At the end, print the following:
# * Number of toys Lily has.
# * Total money she has (money from even birthdays after brother takes ₹1).
# Input
# * Lily’s age (N)
# * Nothing else (price of toys is not needed because we are not selling)
# Output
# * Number of toys
# * Total money (formatted with 2 decimal places)
# Sample TestCase:
# Input
# 10
# Output
# 5
# 150.00
# Explanation:
# Toys → 1,3,5,7,9 → 5 toys.
# Money → 10 + 20 + 30 + 40 + 50 = ₹150. 


age=int(input("Enter the age:"))
start=1
toy=0
money=0
while start<=age:
    if start%2==0:
        money=money+10
    else:
        toy=toy+1
    start=start+1
print(toy)
print(money)