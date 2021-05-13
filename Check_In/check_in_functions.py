# Program: Check-In Functions
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
#   userID, searchType
# Returns:
#   foundIt

def checkUserAccount (userID, searchType):
    
    # Declare Local Variable types (NOT parameters)
    foundIt = False
    createAccountChoice = str()
    checker = str()
    patientList = []
    counter1 = 0
    counter2 = 0
    try:
        file1 = open("database.txt", "r")
    # } end try
    except:
        createUserAccount()
    # } end except
    else:
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
        # } end for
        
        for counter2 in range (len(patientList)):
            if searchType == 1:
                if patientList[counter2][0] == userID:
                    print(patientList[counter2][1] + patientList[counter2][2] + ", thanks for visiting us today.\n")
                    foundIt = True
                # } if end
            # } if end
            else:
                if patientList[counter2][0] == userID:
                    print("First Name: " + patientList[counter2][1])
                    print("Last Name: " + patientList[counter2][2])
                    print("Birth Date: " + patientList[counter2][3])
                    print("Username: " + patientList[counter2][0])
                    print("Address1: " + patientList[counter2][4])
                    print("Address2: " + patientList[counter2][5])
                    print("City: " + patientList[counter2][6])
                    print("State: " + patientList[counter2][7])
                    print("Zipcode: " + patientList[counter2][8])
                    print("Phone Number: " + patientList[counter2][9])
                    print("Email Address: " + patientList[counter2][10] + "\n")
                    foundIt = True
                
                # } end 
            # } end for
        if foundIt == False:
            print("Couldn't find your username in the database")
            print("Would you like to create an account?")
            createAccountChoice = str(input("Enter 1 = Yes / 2 = No : "))

            while createAccountChoice != "1" and createAccountChoice != "2":
                createAccountChoice = str(input("Please, enter the correct number: "))
            # } end while
            if createAccountChoice == "1":
                createUserAccount()
            # } end if
        # } end if

    # Return the return variable, if any
    return foundIt
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
    address1 = str()
    address2 = str()
    city = str()
    state = str()
    zipcode = str()
    phoneNumber = str()
    emailAddress = str()
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
    address1 = input("What is your street address: ")
    address2 = input("APT/Suite/Building#: ")
    city = input("Which City: ")
    state = input("Which State: ")
    zipcode = input("Postal code: ")
    phoneNumber = input("Phone Number in ###-###-#### format: ")
    emailAddress = input("Your Email Address: ")

    if userID in duplicateChecker:
        print("You already have an account!\n")
    else:
        newAccount = [userID, first_name, last_name, birth_date, address1,address2, city,state,str(zipcode),str(phoneNumber),emailAddress.lower()]
        file1 = open("database.txt","a")
        file1.write(str(newAccount)+"/")
        file1.close()
        print("Your username is: " + userID)
        print ("User Account Successfully Created \n")

    

      # so I can test-run the template and not get an error


    # Return the return variable, if any

#} end Function createUserAccount()

