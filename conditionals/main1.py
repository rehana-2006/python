#to find whether the year is leap year or not
#A=int(input("enter a year:"))
#if (A%4==0):
  #  print(" Y")
#else: 
   # print("N")


# A=int(input("Enter a year:"))
# if (A >= 2000 and A<=2100):
#     print(" this is 21th century")
# else:
#     print("this is not 21th century")


def find_grade(mark):
    #Write your code here
    if mark>=75:
     print("You got an A grade")
    elif mark>=60 and mark<75:
     print("You got a B grade")
    elif mark>=45 and mark<60:
     print("You got a C grade")
    elif mark<45:
     print( "You didn't get an A, B or C grade")
    else:
       print("invalid mark")
find_grade(80)
