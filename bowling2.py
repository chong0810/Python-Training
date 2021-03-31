# Program: Bowling
# Description: This program is a second bowling simulation program with logical operators and loops which it will take user's input to calculate and display the score.
#   
# Author: Daniel Hong 
# Date: 20 March 2021
# Revised:  

# list libraries used

# Declare constants (name in ALL_CAPS)

NUM_PINS = int(10)
FRAME_NUM = int(10)
# Declare Variable types (EVERY variable used)
frame_total = int(0)
num_pins_knocked_1 = int(0)
num_pins_knocked_2 = int(0)
game_score = int (0)

# current_frmae = int(0)

# frame_1_ball_1 = int(0)
# frame_1_ball_2 = int(0)

# frame_2_ball_1 = int(0)
# frame_2_ball_2 = int(0)

# frame_3_ball_1 = int(0)
# frame_3_ball_2 = int(0)

# frame_4_ball_1 = int(0)
# frame_4_ball_2 = int(0)

# frame_5_ball_1 = int(0)
# frame_5_ball_2 = int(0)

# frame_6_ball_1 = int(0)
# frame_6_ball_2 = int(0)

# frame_7_ball_1 = int(0)
# frame_7_ball_2 = int(0)

# frame_8_ball_1 = int(0)
# frame_8_ball_2 = int(0)

# frame_9_ball_1 = int(0)
# frame_9_ball_2 = int(0)

# frame_10_ball_1 = int(0)
# frame_10_ball_2 = int(0)



# Beginning of the game 

#looping 10 times
for x in range(FRAME_NUM):

    # resetting variables
    
    frame_total = int(0)
    num_pins_knocked_1 = int(0)
    
    num_pins_knocked_1 = int(input('How many pins were knocked on first attempt?'))
    # validation for first ball
    while num_pins_knocked_1 > NUM_PINS or num_pins_knocked_1 < 0:
        num_pins_knocked_1 = int(input('Please put in a valid number'))
    frame_total = frame_total + num_pins_knocked_1
    # strike?
    if num_pins_knocked_1 == NUM_PINS:
        print("It's a strike! Nice Job!")
    else:
        num_pins_knocked_2 = int(input('How many pins were knocked on second attempt?'))
        # validation for second ball
        while num_pins_knocked_2 > NUM_PINS - num_pins_knocked_1  or num_pins_knocked_2 < 0:
            num_pins_knocked_2 = int(input('Please put in a valid number'))
            # spare?
        if num_pins_knocked_2 == NUM_PINS - num_pins_knocked_1:
              print("It's a spare! Well Done!")             
        else:
            # open frame
            print(".... open frame. Do Better!")
        frame_total = frame_total + num_pins_knocked_2

    # adding game total
    game_score = game_score + frame_total 

    # printing result
    print("Frame    Ball 1    Ball 2   Frame Total     Game Score")
    print("  ", FRAME_NUM, "       ", num_pins_knocked_1, "       ", num_pins_knocked_2, "          " ,frame_total, "          ", game_score)

    



# End Program


