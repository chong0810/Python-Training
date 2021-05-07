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

    print("""Hello, welcome to ACC Lanes.
Here are your shoes.  Pick any ball from the racks.""")

    # Declare Variable types (EVERY variable used in this main program)
    user_answer_game = input("Do you want to play the game?  ")
    user_answer_summary = str
    # Ask the user if they want to play game (repetition)
    while user_answer_game[0].lower() == "y":
        user_answer_summary = input("Do you want a summary?  ")
        play_game(user_answer_summary)

        user_answer_game = input("Do you want to play another game?  ")
    else: print ("""Exiting the game.
    Thanks for playing!""")

# Function play_game()
# Description: This function actually plays one game
#   
# Calls: roll_frames(), print_the_game() 
# Parameters: user_answer_summary
# Returns: none
    
def play_game(user_answer_summary):

    # Declare Local Variable types (NOT parameters)
    
    frames_list = []
    game_stat = []
    for frame_counter in range(NUMBER_OF_FRAMES):
        
        print("Frame ", frame_counter +1)
        
        frames_list = roll_frame(frame_counter)
        
        game_stat.append(frames_list)

        if frame_counter == 0:
            game_stat[frame_counter][4] = game_stat[frame_counter][3]
        if frame_counter != 0:
            game_stat[frame_counter][4] = game_stat[frame_counter][3] + game_stat[frame_counter-1][4]
    
    print_the_game(user_answer_summary,game_stat)

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
    
    current_frame_stat = [frame_counter,0,0,0,0]
    pins_left = NUMBER_OF_PINS
    
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
            print("Ball 1: " , score , "**************STRIKE!")
            return score
        else:
            print("Ball 1: " , score)
            return score


    elif ball_counter == 2 and pins_left !=0:
        score = random.randint(0,pins_left)
        if score == pins_left:
            print("Ball 2: " , score , "**************SPARE!")
            return score

        else:
            print("Ball 2: " , score , "..............open frame")
            return score       
    else:
        score = pins_left
        return score

    # print ( "roll_ball() was executed\n" )  # so I can test-run the template and not get an error


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

def print_the_game(user_answer_summary, game_stat):

    # Declare Local Variable types (NOT parameters)
    frame_counter = 0
    convert_string = str
    # print ( "print_the_game" )  # so I can test-run the template and not get an error
    print("Here is your game summary:")
    print("Frame", "    Ball 1", "    Ball 2", "    Frame Total", "    Total Score")

    
    

    # for frame_counter in range (NUMBER_OF_FRAMES):

    while frame_counter < NUMBER_OF_FRAMES:
        convert_string = '{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame_counter+1, b= game_stat[frame_counter][1], c= game_stat[frame_counter][2], d=game_stat[frame_counter][3], e=game_stat[frame_counter][4])

        print(convert_string)

        if user_answer_summary[0].lower() == 'y':
            
            game_summary = open("gameSummary.txt", "a")
            if frame_counter == 0:
                game_summary.write("\nHere is your game summary:")
                game_summary.write("\nFrame     Ball 1     Ball 2     Frame Total     Total Score\n")
            game_summary.write(convert_string + "\n")
            game_summary.close        

        frame_counter = frame_counter +1

    # Return the return variable, if any

#} Function print_the_game()


# End Program

main()


