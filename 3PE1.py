# Program: Pick A Day
# Description: This program will determine the day from your input from 1 to 7
#   
# Author: Daniel Hong 
# Date: 2/10/21
# Revised: 
#   <revision date> 

# list libraries used

# Declare constants (name in ALL_CAPS)

# Declare Variable types (EVERY variable used)

chooser = int(input("Pick a number between 1 - 7"))

if (chooser == 1):
    print("Monday")
elif (chooser == 2):
    print("Tuesday")
elif (chooser == 3):
    print("Wednesday")
elif (chooser == 4):
    print("Thursday")
elif (chooser == 5):
    print("Friday")
elif (chooser == 6):
    print("Saturday")
elif (chooser == 7):
    print("Sunday")
else:
    print("Wrong input. Exiting Program.")

# End Program
