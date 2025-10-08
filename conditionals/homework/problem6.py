n=int(input("enter the number:"))
match n:
    case n if n%2==0:
        print("even")
    case n if n%2!=0:
        print("odd")
    case _:
        print("invalid input")