# Program: Check-In
# Description: This program allows the users to check-in using their user ID. If there is no user information (new user), the system will ask the users to create an account. Users can also attempt to find their username by providing basic information.
# Author: Chang Yeon Hong
# Date: 12 May 2021
# Revised: 
#   <revision date> 

# list libraries used
import check_in_functions
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
    
    while userInput !="4": 
        print("""Welcome to ACC Check-in Portal.\nPlease select from following options.\n
    1. Check-in\n
    2. Find my ID\n
    3. Create account\n
    4. Exit\n """)

        userInput = str(input("Enter the number: "))

        while userInput != "1" and userInput != "2" and userInput !="3" and userInput !="4":
            userInput = str(input("Please, enter the correct number: "))
        # } end while

        if userInput == "1":
            userName = input("Enter your user name: ")
            checker = check_in_functions.checkUserAccount(userName, 1)
            if checker == True:
                print("You are checked in for your appointment! \n")
            # } end if
            else:
                print("Exiting program")
            # } end else
        # } end if

        elif userInput == "2":
        
            first_name = input("What is your First Name: ")
            last_name = input("What is your Last Name: " )
            birth_date = (input("When is your Birthday in MMDDYYYY format: "))
            userID = (first_name[0]+last_name+str(birth_date)).lower()

            check_in_functions.checkUserAccount(userID, 2)
        # } end elif

        elif userInput == "3":
            check_in_functions.createUserAccount()
        # } end elif
        else:
            print("Exiting Program")
        # } end else






# End Program




main()
