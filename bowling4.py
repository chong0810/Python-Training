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
import random

# Declare global constants (name in ALL_CAPS)

NUMBER_OF_FRAMES = int(10)
NUMBER_OF_PINS = int(10)


def main():

    # Declare Variable types (EVERY variable used in this main program)
    user_answer_game = input("Do you want to play the game?")
    user_answer_summary = str
    # Ask the user if they want to play game (repetition)
    while user_answer_game[0].lower() == "y":
        user_answer_summary = input("Do you want a summary?")
        play_game(user_answer_summary)
        user_answer_game = input("Do you want to play the game?")
    else: print ("Exiting the game.")

# Function play_game()
# Description: This function actually plays one game
#   
# Calls: roll_frames(), print_the_game() 
# Parameters: user_answer_summary
# Returns: none
    
def play_game(user_answer_summary):

    # Declare Local Variable types (NOT parameters)
    
    game_stat = []
    frames_list = []

    print ( "play_game() was executed" )  # so I can test-run the template and not get an error
    
    for frame_counter in range(NUMBER_OF_FRAMES):
        frames_list = roll_frame(Frame_counter)
        print(counter)
        game_stat.append(frames_list)

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

def roll_frame(frame_counter):

    # Declare Local Variable types (NOT parameters)
    
    current_frame_stat = [frame_counter,0,0,0]
    pins_left = NUMBER_OF_PINS
    

    print ( "roll_frame() was executed" )  # so I can test-run the template and not get an error

    for ball_counter in range (1,3):
        pins_left = pins_left - current_frame_stat[1]
        current_frame_stat[ball_counter] = roll_ball(ball_counter, pins_left)
        pins_left = NUMBER_OF_PINS


    current_frame_stat [3] = current_frame_stat [1] + current_frame_stat [2]

    return current_frame_stat

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

def roll_ball(ball_counter, pins_left):

    # Declare Local Variable types (NOT parameters)
    score = int

    if ball_counter == 1:
        score = random.randint(0,pins_left)
        if score == pins_left:
            print("It's a strike!")
        return score
    else:
        score = random.randint(0,pins_left)
        if score == pins_left:
            print("It's a spare")
            return score

        else:
            print("...open frame")
            return score

    print ( "roll_ball() was executed" )  # so I can test-run the template and not get an error


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

def print_the_game(user_answer_summary):

    # Declare Local Variable types (NOT parameters)

    print ( "print_the_game" )  # so I can test-run the template and not get an error


    # Return the return variable, if any

#} Function print_the_game()

# End Program



main()


