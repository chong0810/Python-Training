# Program: Magical Date
# Description: 
#   This program will determine if the input date is magical or not
# Author: Daniel Hong 
# Date: 2/8/21
# Revised: 
#   <revision date> 

# list libraries used

# Declare constants (name in ALL_CAPS)

# Declare Variable types (EVERY variable used)

print("This program will determine if the input date is magical or not")
print("Please put the date in following format mm/dd/yy")

# Ask user to input month
month = int(input("Please enter the month in number: "))

# Ask user to input day
day = int(input("Please enter the day in number : "))

# Ask user to input year
year = int(input("Please enter the the year in number: "))

# Logic
if (month * day == year):
    print("It is magical!")
else:
    print("It is not magical!")


# End Program
