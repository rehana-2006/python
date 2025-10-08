p=input("enter the payment mode:")
match p:
    case "UPI":
        print("you selected UPI payment")
    case "Card":
        print("you selected Debit/Credit Card payment")
    case "NetBanking":
        print("you selected Net Banking")
    case "COD":
        print("you selected cash on delivery")
    case _:
        print("invalid payment mode")