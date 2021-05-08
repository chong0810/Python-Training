# Library name: thinker
#
#
# Functions Included in Library: 
#   think_of_a_number()
#   evaluate_user_guess()
# Author: Chang Yeon Hong
# Date: 08 May 2021
# Revised: 
#   <revision date> 

# list libraries used
import random
# Declare global constants (name in ALL_CAPS)

# Function think_of_a_number()
# Description:
#   generates a random number between a high and low value
#       the random number is the upper limit of the range
#   displays the range for the user to guess:
#       "I'm thinking of a number between" followed by
#       the lower limit and the newly generated upper limit
#
#   generates another random number that is the answer
#       between these lower and upper limits (inclusive: may be either limit value)
#
#   writes the answer to a file for use by evaluate_user_guess()
#
#   returns the generated upper limit
# Calls:
#   none
# Parameters:
#   low_limit       int()
#   high_limit      int()
# Returns:
#   upper_limit     int()

def think_of_a_number(low_limit, high_limit)

    # Declare Local Variable types (NOT parameters)
    upper_limit = int()
    answer = int ()

    upper_limit = random(low_limit, high_limit)
    print(upper_limit)

    print("I'm thinking of a number between ", low_limit, " and " , upper_limit)

    answer = random.randint(low_limit, upper_limit)
    print(answer)


    # Return the return variable, if any
    return upper_limit
# End Function think_of_a_number()


# Function evaluate_user_guess()
# Description:
#   reads the correct answer from the file written by think_of_a_number()
#
#   compares the user's guess to the correct answer
#       if there's any problem, or if the guess is -1
#       return value is "error"
#
#   returns the result as a string:
#       "high", "low", "equal", "error"
# Calls:
#   none
# Parameters:
#   user_guess  int()
# Returns:
#   feedback    str()

def evaluate_user_guess()

    # Declare Local Variable types (NOT parameters)


    # Return the return variable, if any

# End Function evaluate_user_guess()


# End Module thinker

