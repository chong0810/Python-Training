# Program Bowling Simulation
# Description: This program is a bowling simulation. It takes user's input, calculates the total and displays the score.
# # Library <library name> 
# Functions Included in Library: 
#   play_game()
#   roll_frame()
#   roll_ball()
#   prin_the_game()
# Author: Chang Yeon Hong
# Date: May 6, 2021
# Revised: 
#   <revision date> 

# list libraries used

# Declare global constants (name in ALL_CAPS)

NUMBER_OF_FRAMES = int(10)
NUMBER_OF_PINS = int(10)


def main():

    # Declare Variable types (EVERY variable used in this main program)
    user_answer_game = input("Do you want to play the game?")
    user_answer_summary
    # Ask the user if they want to play game (repetition)
    while user_answer_game[0].lower() == "y":
        user_answer_summary = input("Do you want a summary?")
        play_game(user_answer_summary)
        user_answer_game = input("Do you want to play the game?")
    else: print ("Exiting the game.")

# Function play_game()
# Description:
#   
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none
    
def play_game(user_answer_summary):

    # Declare Local Variable types (NOT parameters)
    
    game_stat = []
    
    print ( "play_game" )  # so I can test-run the template and not get an error
    
    roll_frame()

    print_the_game(user_answer_summary)

    


    # Return the return variable, if any

#} Function play_game()

# Function roll_frame()
# Description:
#   just here as a stub: rename and rewrite for real programs
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def roll_frame():

    # Declare Local Variable types (NOT parameters)

    print ( "roll_frame" )  # so I can test-run the template and not get an error

    # Return the return variable, if any

#} Function roll_frame()

# Function roll_ball()
# Description:
#   just here as a stub: rename and rewrite for real programs
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def roll_ball():

    # Declare Local Variable types (NOT parameters)

    print ( "roll_ball" )  # so I can test-run the template and not get an error


    # Return the return variable, if any

#} Function roll_ball()

# Function print_the_game()
# Description:
#   just here as a stub: rename and rewrite for real programs
# Calls:
#   none
# Parameters:
#   none
# Returns:
#   none

def print_the_game():

    # Declare Local Variable types (NOT parameters)

    print ( "print_the_game" )  # so I can test-run the template and not get an error


    # Return the return variable, if any

#} Function print_the_game()

# End Program



main()


