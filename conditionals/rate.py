#movie rating

rating = int(input("Enter your rating"))

match rating:
    case 1:
        print("very bad")
    case 2:
        print("bad")
    case 3:
        print("average")
    case 4:
        print("good")
    case 5:
        print("excellent")
    case _:
        print("invalid rating") 