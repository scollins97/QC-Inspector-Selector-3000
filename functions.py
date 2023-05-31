"""
This is going to pull a random inspector from the database,  It checks to make
sure they don't have a huge lead (if they have 5 more than the average score) 
"""
import random
def chooseTheSelector() :
    #first lets change the background color
    red, green, blue = random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)
    print(red, green, blue)
    return