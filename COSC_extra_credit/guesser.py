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
import thinker

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

def play_a_round(lower_limit, upper_limit):

    # Declare Local Variable types (NOT parameters)
    tries = int(0)
    guess = int()
    think = str("high")

    while think == "high" or think == "low":
        tries = tries + 1 
        guess = make_a_guess(lower_limit, upper_limit)
        think = thinker.evaluate_user_guess(guess)
        if think == "high":
            print("The number you guessed is higher than the answer.")
        # } end if
        elif think == "low":
            print("The number you guessed is lower than the answer.")
        # } end elif
    # } end while

    if think == "error":
        tries = -1
    # } end if


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

def make_a_guess(low, high):

    # Declare Local Variable types (NOT parameters)
    try:
        my_guess = int(input("I'm guessing "))
        
        while my_guess < low or my_guess > high:
            print("Please guess a number between ", low, " and ", high)
            my_guess = int(input("I'm guessing "))
    except:
        my_guess = -1
   

    # Return the return variable, if any
    return my_guess
# End Function make_a_guess()


# End Module guesser

