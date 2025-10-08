sub=input("Enter the subject(science/commerce/arts):")
match sub:
    case "science":
        path=input("Choose the path(medical/Engineering):")
        match path:
            case "medical":
                print("chosen path:science->medical")
            case "Engineering":
                print("chosen path:science->engineering")
            case _:
                print("invalid input")
    case "commerce":
        path=input("Choose the path(CA/B.Com):")
        match path:
            case "CA":
                print("chosen path:commerce->CA")
            case "B.Com":
                print("chosen path:commerce->B.Com")
            case _:
                print("invalid input")
    case "arts":
        path=input("Choose the path(history/literature):")
        match path:
            case "history":
                print("chosen path:science->history")
            case "literature":
                print("chosen path:science->literature")
            case _:
                print("invalid input")
    case _:
        print("invalid input")