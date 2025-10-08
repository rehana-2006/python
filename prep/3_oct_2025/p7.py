# Multi-Item Shopping Discount
# * Price > 100 → 10% discount
# * Price 50–100 → 5% discount
# * Price <50 → no discount
# Print discounted price per item
# Test cases with their output:
# 200 → 180
# 80 → 76
# 40 → 40
# 150 → 135

p=int(input("enter the price:"))
if p>0 and p<50:
    print("no discount")
elif p>=50 and p<=100:
    d=p*5/100
    print("The discounted price is",d)
elif p>100:
    d=p*10/100
    print("the discounted price is",d)
else:
    print("Invalid input")