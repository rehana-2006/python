# 5. Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:
# It has at least 8 characters and  atleast one special character (!@#$%^&*).
# Print whether the password is strong or not.
# Input:
# Password: my@password
# Output:
# Password is strong
# Input:
# Password: python123
# Output:
# Password is not strong

def passwords(n):
    special_characters = "!@#$%^&*"
    if len(n) < 8:
        print("Password is not strong")
    else:
        for char in n:
            if char in special_characters:
                print("Password is strong")
                break
        else:
            print("Password is not strong")
passwords("my@password")
passwords("python123")
