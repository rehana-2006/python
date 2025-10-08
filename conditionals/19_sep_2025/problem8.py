t=int(input("Enter the show time (in 24-hour format):"))
if t>=9 and t<12:
    print("morning show")
elif t>=12 and t<16:
    print("matinee show")
elif t>=16 and t<20:
    print("evening show")
elif(t>=20 and t<=24 ) or( t>=0 and t<=8):
    print("night show")
else:
    print("invalid input")