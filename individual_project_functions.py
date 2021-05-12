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
    foundIt = False
    createAccountChoice = str()
    checker = str()
    patientList = []
    counter1 = 0
    counter2 = 0

    file1 = open("database.txt", "r")

    checker = file1.read()
    patientList = checker.split("/")
    patientList.pop()

    for counter1 in range (len(patientList)):
        cutter = str()
        newList = []

        cutter = patientList[counter1]
        cutter = cutter.replace("[","")
        
        cutter = cutter.replace("]","")
        
        cutter = cutter.replace("'","")
        
        
        newList = cutter.split(",")
        
        patientList[counter1] = newList
        
    for counter2 in range (len(patientList)):
        
        if patientList[counter2][0] == userID:
            print("First Name: " + patientList[counter2][1])
            print("Last Name: " + patientList[counter2][2])
            print("Birth Date: " + patientList[counter2][3])
            print("Username: " + patientList[counter2][0])
            foundIt = True
    if foundIt == False:
        print("Couldn't find your username in the database")
        print("Would you like to create an account?")
        createAccountChoice = str(input("Enter 1 = Yes / 2 = No"))

        while createAccountChoice != "1" and createAccountChoice != "2":
            createAccountChoice = str(input("Please, enter the correct number: "))
        if createAccountChoice == "1":
            createUserAccount()

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

