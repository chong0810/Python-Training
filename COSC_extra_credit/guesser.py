# Library name: guesser
#
# Functions Included in Library: 
#   play_a_round()
#   make_a_guess()
# Author: Chang Yeon Hong
# Date: 8 May 2021
# Revised: 
#   <revision date> 

# list libraries used
import thinker, random

# Declare global constants (name in ALL_CAPS)

# Function play_a_round()
# Description:
#   Plays the guessing game round:
#       guesses a number between the lower and upper limits
#       uses the thinker's evaluate routine to check correctness
#       keeps guessing until the evaluator returns a match or error indicator
#   returns the number of tries
#       ( tries is -1 if an error occured )
# Calls:
#   make_a_guess()
#   thinker.evaluate_user_guess()
# Parameters:
#   lower_limit     int()
#   upper_limit     int()
# Returns:
#   tries           int()

def play_a_round(lower_limit, upper_limit)

    # Declare Local Variable types (NOT parameters)
    tries = int()

    thinker.evaluate_user_guess()
    make_a_guess()


    # Return the return variable, if any

    return tries
# End Function play_a_round()


# Function make_a_guess()
# Description:
#   makes a single guess for a number between the lower and upper limits provided
#       using whatever method seems to best
#
#   displays "I'm guessing" followed by the guess
#
#   returns the guess ( -1 if there's any error )
# Calls:
#   none
# Parameters:
#   low         int()
#   high        int()
# Returns:
#   my_guess    int()

def make_a_guess(low, high)

    # Declare Local Variable types (NOT parameters)
    my_guess = int()
    my_guess = random.randint(low,high)
    # Return the return variable, if any
    return my_guess
# End Function make_a_guess()


# End Module guesser

