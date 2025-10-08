# A shopkeeper has n mangoes.
# He wants to pack them into baskets, with 5 mangoes in each basket.
# Write a program to calculate:
# * How many full baskets can be made
# * How many mangoes will be left
# Sample Input:
# 23
# Sample Output:
# Full Basket is 4
# Left Over mangoes is 3

n=int(input("enter the number:"))
start=0
b=0
m=n
if n>0:
    while start<=n:
        m=m-5
        b=b+1
        start=start+6
    print("Full Basket is ",b)
    print("Left Over Mangoes ",m)
else:
    print("Invalid input")