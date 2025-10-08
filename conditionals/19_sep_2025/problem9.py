value=int(input("Enter the value in kilometers:"))
print("conversion choice: \n 1->convert to meters \n 2->convert to centimeters \n 3->convert to millimeter \n 4->convert to miles")
km=int(input("enter your choice(1-4):"))
match km:
    case 1:
        print(value*1000)
    case 2:
        print(value*100000)
    case 3:
        print(value*1000000)
    case 4:
        print(value*0.621371)
    case _:
        print("invalid conversion")