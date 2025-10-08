# A child has n candies and eats one candy each day until all are finished.
# Write Python program to print how many candies the child ate and how many are left each day.
# Sample Input:
# 3
# Sample Output:
# Day 1 = 2 left
# Day 2 = 1 left
# Day 3 = 0 left

n=int(input("Enter the number of candies:"))
d=0
l=n
for i in range(1,n+1,1):
    d=d+1
    l=l-1
    print("day",d,"=",l,"left")