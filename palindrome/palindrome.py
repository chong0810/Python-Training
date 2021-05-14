# Program Palindrome 
# Description: This program will tell if the word or the sentence is a palindrome.
# Author: Chang Yeon Hong
# Date: 13 May 2021
# Revised: 
#   <revision date> 

# list libraries used
import palindrome_functions
# Declare global constants (name in ALL_CAPS)

def main():

# Declare Variable types (EVERY variable used in this main program)
    palindromeChecker = str(input("Put in the word or sentence to check if it is palindrome: "))
    palindrome_functions.checkPalindrome(palindromeChecker)
        

# End Program

main()
