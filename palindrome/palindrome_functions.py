# Program: Palindrome_functions 
# Description: 
#   template with a stub function
# Author: <your name> 
# Date: <today’s date>
# Revised: 
#   <revision date> 

# list libraries used

# Declare global constants (name in ALL_CAPS)

# Function stub()
# Description:
#   just here as a stub: rename and rewrite for real programs
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def checkPalindrome(palindromeChecker):

    # Declare Local Variable types (NOT parameters)
    palindromeWord = palindromeChecker.lower()
    palindromeBackward = str()

    palindromeWord = palindromeWord.replace(" ", "")
    print(palindromeWord)
    palindromeWord = palindromeWord.replace(",","")
    print(palindromeWord)
    palindromeWord = palindromeWord.replace(".","")
    print(palindromeWord)
    palindromeWord = palindromeWord.replace(";","")
    print(palindromeWord)
    palindromeWord = palindromeWord.replace(":","")
    print(palindromeWord)
    palindromeWord = palindromeWord.replace("'","")
    print(palindromeWord)
    palindromeWord = palindromeWord.replace('"',"")
    print(palindromeWord)
    palindromeWord = palindromeWord.replace("?","")
    print(palindromeWord)
    palindromeWord = palindromeWord.replace("!","")
    print(palindromeWord)

    palindromeBackward = palindromeWord[::-1]
    print(palindromeBackward)

    if palindromeWord == palindromeBackward:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
    
    # so I can test-run the template and not get an error


    # Return the return variable, if any

#} Function stub()

