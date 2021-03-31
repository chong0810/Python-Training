# Program: Bowling
# Description: This program is a second bowling simulation program with logical operators and loops which it will take user's input to calculate and display the score.
#   
# Author: Daniel Hong 
# Date: 20 March 2021
# Revised:  

# list libraries used

# Declare constants (name in ALL_CAPS)

NUM_PINS = int(10)
NUM_FRAMES = int(10)

# Declare Variable types (EVERY variable used)
current_frame = int(0)
frame_total = int (0)
total_score = int(0)
frame_1_ball_1 = int(0)
frame_1_ball_2 = int(0)
frame_2_ball_1 = int(0)
frame_2_ball_2 = int(0)
frame_3_ball_1 = int(0)
frame_3_ball_2 = int(0)
frame_4_ball_1 = int(0)
frame_4_ball_2 = int(0)
frame_5_ball_1 = int(0)
frame_5_ball_2 = int(0)
frame_6_ball_1 = int(0)
frame_6_ball_2 = int(0)
frame_7_ball_1 = int(0)
frame_7_ball_2 = int(0)
frame_8_ball_1 = int(0)
frame_8_ball_2 = int(0)
frame_9_ball_1 = int(0)
frame_9_ball_2 = int(0)
frame_10_ball_1 = int(0)
frame_10_ball_2 = int(0)


# Beginning of the game 
# Looping 10 times for the scores
for frame in range(NUM_FRAMES):

    # frame 1
    if frame == 0:
        print("This is frame #", frame + 1)
        frame_1_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_1_ball_1 > NUM_PINS or frame_1_ball_1 < 0:
            frame_1_ball_1 = int(input('Please put in a valid number : '))
        
        if frame_1_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_1_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_1_ball_2 > NUM_PINS - frame_1_ball_1  or frame_1_ball_2 < 0:
                frame_1_ball_2 = int(input('Please put in a valid number'))
            # spare?
            if frame_1_ball_2 == NUM_PINS - frame_1_ball_1:
                print("It's a spare! Well Done!")             
            else:
            # open frame
                print(".... open frame. Do Better!")

    # frame 2
    if frame == 1:
        print("This is frame #", frame + 1)
        frame_2_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_2_ball_1 > NUM_PINS or frame_2_ball_1 < 0:
            frame_2_ball_1 = int(input('Please put in a valid number : '))
    
        if frame_2_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_2_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_2_ball_2 > NUM_PINS - frame_2_ball_1  or frame_2_ball_2 < 0:
                frame_2_ball_2 = int(input('Please put in a valid number'))
            # spare?
            if frame_2_ball_2 == NUM_PINS - frame_2_ball_1:
                print("It's a spare! Well Done!")             
            else:
            # open frame
                print(".... open frame. Do Better!")

    # frame 3
    if frame == 2:
        print("This is frame #", frame + 1)
        frame_3_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_3_ball_1 > NUM_PINS or frame_3_ball_1 < 0:
            frame_3_ball_1 = int(input('Please put in a valid number : '))
    
        if frame_3_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_3_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_3_ball_2 > NUM_PINS - frame_3_ball_1  or frame_3_ball_2 < 0:
                frame_3_ball_2 = int(input('Please put in a valid number'))
            # spare?
            if frame_3_ball_2 == NUM_PINS - frame_3_ball_1:
                print("It's a spare! Well Done!")             
            else:
                # open frame
                print(".... open frame. Do Better!")

    # frame 4
    if frame == 3:
        print("This is frame #", frame + 1)
        frame_4_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_4_ball_1 > NUM_PINS or frame_4_ball_1 < 0:
            frame_4_ball_1 = int(input('Please put in a valid number : '))
    
        if frame_4_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_4_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_4_ball_2 > NUM_PINS - frame_4_ball_1  or frame_4_ball_2 < 0:
                frame_4_ball_2 = int(input('Please put in a valid number'))
                # spare?
            if frame_4_ball_2 == NUM_PINS - frame_4_ball_1:
                 print("It's a spare! Well Done!")             
            else:
                # open frame
                print(".... open frame. Do Better!")

    # frame 5
    if frame == 4:
        print("This is frame #", frame + 1)
        frame_5_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_5_ball_1 > NUM_PINS or frame_5_ball_1 < 0:
            frame_5_ball_1 = int(input('Please put in a valid number : '))
    
        if frame_5_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_5_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_5_ball_2 > NUM_PINS - frame_5_ball_1  or frame_5_ball_2 < 0:
                frame_5_ball_2 = int(input('Please put in a valid number'))
            # spare?
            if frame_5_ball_2 == NUM_PINS - frame_5_ball_1:
                print("It's a spare! Well Done!")             
            else:
                # open frame
                print(".... open frame. Do Better!")

    # frame 6
    if frame == 5:
        print("This is frame #", frame + 1)
        frame_6_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_6_ball_1 > NUM_PINS or frame_6_ball_1 < 0:
            frame_6_ball_1 = int(input('Please put in a valid number : '))
    
        if frame_6_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_6_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_6_ball_2 > NUM_PINS - frame_6_ball_1  or frame_6_ball_2 < 0:
                frame_6_ball_2 = int(input('Please put in a valid number'))
            # spare?
            if frame_6_ball_2 == NUM_PINS - frame_6_ball_1:
                print("It's a spare! Well Done!")             
            else:
            # open frame
                print(".... open frame. Do Better!")

    # frame 7
    if frame == 6:
        print("This is frame #", frame + 1)
        frame_7_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_7_ball_1 > NUM_PINS or frame_7_ball_1 < 0:
            frame_7_ball_1 = int(input('Please put in a valid number : '))
    
        if frame_7_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_7_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_7_ball_2 > NUM_PINS - frame_7_ball_1  or frame_7_ball_2 < 0:
                frame_7_ball_2 = int(input('Please put in a valid number'))
            # spare?
            if frame_7_ball_2 == NUM_PINS - frame_7_ball_1:
                print("It's a spare! Well Done!")             
            else:
                # open frame
                print(".... open frame. Do Better!")

    # frame 8
    if frame == 7: 
        print("This is frame #", frame + 1)
        frame_8_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_8_ball_1 > NUM_PINS or frame_8_ball_1 < 0:
            frame_8_ball_1 = int(input('Please put in a valid number : '))
    
        if frame_8_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_8_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_8_ball_2 > NUM_PINS - frame_8_ball_1  or frame_8_ball_2 < 0:
                frame_8_ball_2 = int(input('Please put in a valid number'))
            # spare?
            if frame_8_ball_2 == NUM_PINS - frame_8_ball_1:
                print("It's a spare! Well Done!")             
            else:
            # open frame
                print(".... open frame. Do Better!")

    # frame 9
    if frame == 8:
        print("This is frame #", frame + 1)
        frame_9_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_9_ball_1 > NUM_PINS or frame_9_ball_1 < 0:
            frame_9_ball_1 = int(input('Please put in a valid number : '))
    
        if frame_9_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_9_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_9_ball_2 > NUM_PINS - frame_9_ball_1  or frame_9_ball_2 < 0:
                frame_9_ball_2 = int(input('Please put in a valid number'))
            # spare?
            if frame_9_ball_2 == NUM_PINS - frame_9_ball_1:
                print("It's a spare! Well Done!")             
            else:
            # open frame
                print(".... open frame. Do Better!")

    # frame 10
    if frame == 9:
        print("This is frame #", frame + 1)
        frame_10_ball_1 = int(input('How many pins were knocked down on the first attempt? : '))
        while frame_10_ball_1 > NUM_PINS or frame_10_ball_1 < 0:
            frame_10_ball_1 = int(input('Please put in a valid number : '))
        if frame_10_ball_1 == NUM_PINS:
            print("It's a strike! Nice Job!")
        else:
            frame_10_ball_2 = int(input('How many pins were knocked down on second attempt?'))
            # validation for second ball
            while frame_10_ball_2 > NUM_PINS - frame_10_ball_1  or frame_10_ball_2 < 0:
                frame_10_ball_2 = int(input('Please put in a valid number'))
            # spare?
            if frame_10_ball_2 == NUM_PINS - frame_10_ball_1:
              print("It's a spare! Well Done!")             
            else:
            # open frame
                print(".... open frame. Do Better!")

# Summary
# Printing out Results
print("Frame", "    Ball 1", "    Ball 2", "    Frame Total", "    Total Score")

for frame in range (NUM_PINS):
    
    frame_total = int(0)

    if frame == 0:
        frame_total = frame_1_ball_1 + frame_1_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_1_ball_1, c= frame_1_ball_2, d=frame_total, e=total_score))
    
    if frame == 1:
        frame_total = frame_2_ball_1 + frame_2_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_2_ball_1, c= frame_2_ball_2, d=frame_total, e=total_score))

    if frame == 2:
        frame_total = frame_3_ball_1 + frame_3_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_3_ball_1, c= frame_3_ball_2, d=frame_total, e=total_score))


    if frame == 3:
        frame_total = frame_4_ball_1 + frame_4_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_4_ball_1, c= frame_4_ball_2, d=frame_total, e=total_score))

    if frame == 4:
        frame_total = frame_5_ball_1 + frame_5_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_5_ball_1, c= frame_5_ball_2, d=frame_total, e=total_score))
    
    if frame == 5:
        frame_total = frame_6_ball_1 + frame_6_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_6_ball_1, c= frame_6_ball_2, d=frame_total, e=total_score))
    
    if frame == 6:
        frame_total = frame_7_ball_1 + frame_7_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_7_ball_1, c= frame_7_ball_2, d=frame_total, e=total_score))
    
    if frame == 7:
        frame_total = frame_8_ball_1 + frame_8_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_8_ball_1, c= frame_8_ball_2, d=frame_total, e=total_score))
    
    if frame == 8:
        frame_total = frame_9_ball_1 + frame_9_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_9_ball_1, c= frame_9_ball_2, d=frame_total, e=total_score))
    
    if frame == 9:
        frame_total = frame_10_ball_1 + frame_10_ball_2
        total_score = total_score + frame_total
        print('{a:>5} {b:>10} {c:>10} {d:>15} {e:>15}'.format(a = frame+1, b= frame_10_ball_1, c= frame_10_ball_2, d=frame_total, e=total_score))

print("Thanks for playing!")

# End Program


