#getting input from the user
radius=input("Enter the radius of the cylinder:")
print("you have entered radius as =",radius)

print("Enter the height of the cylinder")
height = input()

print("Cylinder dimensions are",radius,height)

#print(type(radius))
#print(type(height))

#new variable
r = int(radius)
h = int(height)
pi = 3.14

#volume estimate
v = pi*r*r*h
print("volume:",v)