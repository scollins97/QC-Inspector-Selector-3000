"""
This is going to pull a random inspector from the database,  It checks to make
sure they don't have a huge lead (if they have 5 more than the average score) 
"""
import random
import SQL_Handler

def getRandomInspectorWithinReason() :
    
    return

def randomcolor() :
    #first lets get random RGB values
    red, green, blue = random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)
    #converting the RGB values to a hexadecimal so computer can read it
    color = f'#{red:02x}{green:02x}{blue:02x}'
    return color