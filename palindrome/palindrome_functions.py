# Program: Palindrome_functions 
# Description: This is Palindrome_functions module that it will check if the word or sentence is palindrome or not.
# Author: Chang Yeon Hong
# Date: 13 May 2021
# Revised: 
#   <revision date> 

# list libraries used

# Declare global constants (name in ALL_CAPS)

# Function checkPalindrome()
# Description: This function will check if the word or sentence is a palindrome or not
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def checkPalindrome():

    # Declare Local Variable types (NOT parameters)
    infile = str()
    #read string_file.txt
    try:
        infile = open("string_file.txt", 'r')
    except:
        print("There was an error reading string_file.txt")
    else:
        stringList = infile.readlines()
        infile.close()

        for line in stringList:
            palindromeWord = line.lower()
            whatSentence = palindromeWord
            whatSentence = whatSentence.replace("\n", "")
            palindromeBackward = str()

        #these lines will eliminate special characters
            palindromeWord = palindromeWord.replace("-", "")
            palindromeWord = palindromeWord.replace(" ", "")
            palindromeWord = palindromeWord.replace(",","")
            palindromeWord = palindromeWord.replace(".","")
            palindromeWord = palindromeWord.replace(";","")
            palindromeWord = palindromeWord.replace(":","")
            palindromeWord = palindromeWord.replace("'","")
            palindromeWord = palindromeWord.replace('"',"")
            palindromeWord = palindromeWord.replace("?","")
            palindromeWord = palindromeWord.replace("!","")
            palindromeWord = palindromeWord.replace("\n","")
        
            #this line will flip the word or sentence
            palindromeBackward = palindromeWord[::-1]
        
            #this will determine if the word or sentence is palindrome
            if palindromeWord == palindromeBackward:
                print(whatSentence + " \n" + "It is a palindrome.\n")
            # } end if
            else:
                print(whatSentence + " \n" + "It is not a palindrome.\n")
            # } end else
        # } end for
    


    # Return the return variable, if any

#} Function checkPalindrome()

