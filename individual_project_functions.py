# Program: Basic Login Functions
# Description: This is a list of functions that will be used for checking in the patient.
# Author: Chang Yeon Hong
# Date: 12 May 2021
# Revised: 
#   <revision date> 

# list libraries used
# Declare global constants (name in ALL_CAPS)

# Function checkUserAccount()
# Description: This will check if the user already has an account
# Calls:
#   createUserAccount()
# Parameters:
#   userID
# Returns:
#   none

def checkUserAccount (userID):
    
    # Declare Local Variable types (NOT parameters)
    checker = str()
    patientList = []
    file1 = open("database.txt", "r")

    checker = file1.read()
    patientList = checker.split("/")

    print(patientList)


    

    print ( "checkUserAccount" )  # so I can test-run the template and not get an error


    # Return the return variable, if any

#} end Function createUserAccount()

# Function createUserAccount()
# Description: This will check if the user already has an account
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def createUserAccount ():

    # Declare Local Variable types (NOT parameters)
    first_name = str()
    last_name = str()
    birth_date = int()
    userID = str()
    duplicateChecker = str()
    file1 = str()
    newAccount = []

    try:
        file1 = open("database.txt","r")

    except:
        print("There is no data in the database. Please create one.")
    else:
        duplicateChecker = file1.read()
        file1.close()
    
    first_name = input("What is your First Name: ")
    last_name = input("What is your Last Name: " )
    birth_date = (input("When is your Birthday in MMDDYYYY format: "))
    userID = (first_name[0]+last_name+str(birth_date)).lower()

    print(duplicateChecker)

    if userID in duplicateChecker:
        print("You already have an account!")
    else:
        newAccount = [userID, first_name, last_name, birth_date]
        print(newAccount)
        file1 = open("database.txt","a")
        file1.write(str(newAccount)+"/")
        file1.close()


    

    print ( "createUserAccount" )  # so I can test-run the template and not get an error


    # Return the return variable, if any

#} end Function createUserAccount()

# def findMyAccount ():
#     checker = str()
#     file1 = open("database.txt","r")
#     checker = file1.read()
#     print(checker)

    
#     # Declare Local Variable types (NOT parameters)
#     print("Find my Account")  # so I can test-run the template and not get an error


#     # Return the return variable, if any

# #} end Function findMyAccount()

