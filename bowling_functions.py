# Program Bowling Functions
# Description: This is module for bowling functions
# Author: Chang Yeon Hong
# Date: May 6, 2021
# Revised: 
#   <revision date> 
# list libraries used

import random

# Function play_game()
# Description: This is a function that starts the bowling game
# Calls:
#   roll_frame()
#   print_the_game()
# Parameters:
#   frame_num, pin_num ,user_answer_summary
# Returns:
#   none


def play_game(frame_num, pin_num ,user_answer_summary):

    # Declare Local Variable types (NOT parameters)
    
    frames_list = []
    game_stat = []
    for frame_counter in range(frame_num):
        
        print("Frame ", frame_counter +1)
        
        frames_list = roll_frame(frame_counter, pin_num)
        
        game_stat.append(frames_list)

        if frame_counter == 0:
            game_stat[frame_counter][4] = game_stat[frame_counter][3]
        #} end if
        if frame_counter != 0:
            game_stat[frame_counter][4] = game_stat[frame_counter][3] + game_stat[frame_counter-1][4]
        #} end if
    # } end for

    print_the_game(user_answer_summary,game_stat, frame_num)

    # Return the return variable, if any

#} end Function play_game()

# Function roll_frame()
# Description: This function simulates each frame
# Calls:
#   roll_ball()
# Parameters:
#   frame_counter, pin_num
# Returns:
#   current_frame stat

def roll_frame(frame_counter, pin_num):

    # Declare Local Variable types (NOT parameters)
    
    current_frame_stat = [frame_counter,0,0,0,0]
    pins_left = pin_num
    
    for ball_counter in range (1,3):
        pins_left = pins_left - current_frame_stat[1]
        current_frame_stat[ball_counter] = roll_ball(ball_counter, pins_left)
        pins_left = pin_num
    # } end for 


    current_frame_stat [3] = current_frame_stat [1] + current_frame_stat [2]

    return current_frame_stat

    # Return the return variable, if any

#} end Function roll_frame()

# Function roll_ball()
# Description: This function plays the role of tossing the ball
# Calls:
#   random.randint()
# Parameters:
#   ball_counter, pins_left
# Returns:
#   score

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
        # } end if-else
    
    elif ball_counter == 2 and pins_left !=0:
        score = random.randint(0,pins_left)
        if score == pins_left:
            print("Ball 2: " , score , "**************SPARE!")
            return score
        # } end if

        else:
            print("Ball 2: " , score , "..............open frame")
            return score       
        # } end else
    else:
        score = pins_left
        return score
    # } end it-elif-else

    # Return the return variable, if any

# } end Function roll_ball()

# Function print_the_game()
# Description:
#   This function prints out the summary of the game and user chooses if he or    she wants to save the summary in text file.
# Calls:
#   String.lower()
#   open()
#   file.write()
#   file.close()
# Parameters:
#   user_answer_summary, game_stat, frame_num
# Returns:
#   none

def print_the_game(user_answer_summary, game_stat, frame_num):

    # Declare Local Variable types (NOT parameters)
    frame_counter = 0
    convert_string = str
    
    print("Here is your game summary:")
    print("Frame", "    Ball 1", "    Ball 2", "    Frame Total", "    Total Score")

    
    while frame_counter < frame_num:
        convert_string = '{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame_counter+1, b= game_stat[frame_counter][1], c= game_stat[frame_counter][2], d=game_stat[frame_counter][3], e=game_stat[frame_counter][4])

        print(convert_string)

        if user_answer_summary[0].lower() == 'y':
            try:
                game_summary = open("gameSummary.txt", "a")
            # } end try
            except:
                print("There was an error")
            # } end except
            else:
                if frame_counter == 0:
                    game_summary.write("\nHere is your game summary:")
                    game_summary.write("\nFrame     Ball 1     Ball 2     Frame Total     Total Score\n")
                # } end if
            # } end else    
            game_summary.write(convert_string + "\n")
            game_summary.close()        
        # } end if

        frame_counter = frame_counter +1
    # } end while
    # Return the return variable, if any

#} Function print_the_game()