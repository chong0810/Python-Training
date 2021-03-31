# Program: Ocean Rising 
# Description: This is a ocean rising calculator.
#   
# Author: Daniel Hong 
# Date: 3/3/2021
# Revised: 
#   <revision date> 

# list libraries used

# Declare constants (name in ALL_CAPS)

Rising_Rate = 1.6

# Declare Variable types (EVERY variable used)

total_Level = 0
year = 2021

for x in range (1,26):
    year = year + 1
    total_Level = total_Level + Rising_Rate
    print ("This is year ",year, " and ocean rose ", Rising_Rate,"mm and total risen level from year 2021 is ", round(total_Level,1),"mm")


# End Program
    