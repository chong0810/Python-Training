# Program Bowling Simulation
# Description: This program is a bowling simulation. It takes user's input, calculates the total and displays the score.
#   Library : bowling_functions, random
# Functions Included in Library: 
#   play_game()
#   roll_frame()
#   roll_ball()
#   print_the_game()
#   random.int()
# Author: Chang Yeon Hong
# Date: May 6, 2021
# Revised: 
#   <revision date> 

# list libraries used
import bowling_functions

# Declare global constants (name in ALL_CAPS)

NUMBER_OF_FRAMES = int(10)
NUMBER_OF_PINS = int(10)


def main():

    print("""Hello, welcome to ACC Lanes.
Here are your shoes.  Pick any ball from the racks.""")

    # Declare Variable types (EVERY variable used in this main program)
    user_answer_game = input("Do you want to play the game?  ")
    user_answer_summary = str
    # Ask the user if they want to play game (repetition)
    while user_answer_game[0].lower() == "y":
        user_answer_summary = input("Do you want a summary?  ")
        bowling_functions.play_game(NUMBER_OF_FRAMES, NUMBER_OF_PINS,user_answer_summary)

        user_answer_game = input("Do you want to play another game?  ")
    else: print ("""Exiting the game.
    Thanks for playing!""")


# End Program

main()