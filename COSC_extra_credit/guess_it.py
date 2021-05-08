# Program guess_it
# Description: 
#   plays a number-guessing game
# Author: Carl Gregory
# Date: 12 April 2021
# Revised: 
#   <revision date> 

# list libraries used
import thinker, guesser, os

# Declare global constants (name in ALL_CAPS)
RANGE_LOWER_LIMIT = 0
RANGE_UPPER_LIMIT = 100

DEBUG = False

def main():

    # Declare Variable types (EVERY variable used in this main program)
    answer = ""
    errorMessage = ""
    num_tries = int()

    answer = input( "Would you like to play a game (Y/n)? " )
    print()
    while ( answer.lower() != 'n' ):

        os.system("cls")

        print( "Largest number will be between", RANGE_LOWER_LIMIT, "and", RANGE_UPPER_LIMIT )
        print( "Computer will think of a number between", RANGE_LOWER_LIMIT, "and the largest number" )
        print()

        if ( DEBUG ):   # this will run without catching Exceptions
                        # so I can see errors in command-line mode
            num_tries = play_game()
            
        else:
            try:
                num_tries = play_game()
            except Exception as errorMessage:
                print( errorMessage )
            else:
                print()
                if ( num_tries < 0 ):
                    print( "!!!!!!!!!!! What happened ???????????" )
                else:
                    print( "***************** That's right!!", end='' )
                    print( " You guessed it in", num_tries, "tries!!" )
                    print( "Now wasn't that fun?" )
                #} if
                print()
            #} try

        #} if
                
        answer = input( "Would you like to play another game (Y/n)? " )
        
    #} while

# End Program

# Function play_game()
# Description:
#   Plays the guessing game: guess a number between the lower and upper limits
#   returns the number of tries    
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   tries       int()

def play_game ():

    # Declare Local Variable types (NOT parameters)
    upper_limit = int()
    lower_limit = int()
    my_guess = int()
    computer_tries = int()
    human_tries = int()
    feedback = str()
    still_guessing = bool()
    
    # "thinker" chooses an upper limit for the guess
    # i.e., it will be "between 0 and 25" or "between 0 and 183"
    # when presented to the guesser
    # and returns that upper limit here
    lower_limit = RANGE_LOWER_LIMIT
    upper_limit = thinker.think_of_a_number( lower_limit, RANGE_UPPER_LIMIT )
    
    computer_tries = guesser.play_a_round( lower_limit, upper_limit )

    # Return the return variable, if any
    return computer_tries

# End Function play_game()

main()
