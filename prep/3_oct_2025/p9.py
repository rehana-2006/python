# Taxi charges:
# * First 10 km → ₹15/km
# * Next 20 km → ₹12/km
# * Beyond 30 km → ₹10/km
# Estimate the Taxi charges based on the input and print the output.
# Sample Input:
# 15  → 180
# 35 → 350
# 10 → 150

km=int(input("Enter the distance:"))
if km>0 and km<=10:
    f=km*15
    print(f)
elif km>10 and km<=20:
    f=(10*15)+(km-10)*12
    print(f)
elif km>20 and km<=30:
    f=(10*15)+(20*12)+(km-30)*10
    print(f)
else:
    print("Invalid input")