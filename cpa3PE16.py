# Program Leap Year Checker 
# Description: 
#   This program will check if input year is leap year or not. 
# Author: Daniel Hong 
# Date: 2/7/21
# Revised: 
#   <revision date> 

# list libraries used

# Declare constants (name in ALL_CAPS)

# Declare Variable types (EVERY variable used)

year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("It is a leap year")
       else:
           print("It is not a leap year")
   else:
       print("It is a leap year")
else:
   print("It is not a leap year")


# End Program
