# Program: Basic Login
# Description: This program will  
# Author: Chang Yeon Hong
# Date: 12 May 2021
# Revised: 
#   <revision date> 

# list libraries used
import individual_project_functions
# Declare global constants (name in ALL_CAPS)


def main():
    
    # Declare Variable types (EVERY variable used in this main program)

    userInput = str()
    userName = str()
    first_name = str()
    last_name = str()
    birth_date = int()
    userInput = str()
    checker = True
    
    
    print("""Welcome to ACC Hospital Check-in Portal.\nPlease select from following options.\n
    1. Check-in\n
    2. Find my ID\n
    3. Exit\n """)

    userInput = str(input("Enter the number: "))

    while userInput != "1" and userInput != "2" and userInput !="3":
        userInput = str(input("Please, enter the correct number: "))
    # } end while

    if userInput == "1":
        userName = input("Enter your user name: ")
        checker = individual_project_functions.checkUserAccount(userName)
        if checker == True:
            print("Thanks for checking in!")
        # } end if
        else:
            print("Exiting program")
        # } end else

    elif userInput == "2":
        
        first_name = input("What is your First Name: ")
        last_name = input("What is your Last Name: " )
        birth_date = (input("When is your Birthday in MMDDYYYY format: "))
        userID = (first_name[0]+last_name+str(birth_date)).lower()

        individual_project_functions.checkUserAccount(userID)
    else:
        print("Exiting Program")






# End Program




main()
