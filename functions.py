import random
import sqlFunctions

#define what an inspector is so that the data can be manipulated
class Inspector:
    #attributes
    workId = 0
    name = ""
    score = 0

    #methods
    def __init__(self, workId, name, score):
        self.workId = workId
        self.name = name
        self.score = score
        
#this function pulls an inspector from database, and return it as long as their score isn't too much 
def getRandomInspectorWithinReason() :
    notAValidNameYet = True
    #this loop will keep going until the name it randomly pulls meets the score criteria
    while notAValidNameYet == True :
        row = sqlFunctions.selectRandomInspector() 
        print(row)
        #Creating inspector object
        inspector = Inspector(row[0],row[1],row[2])
        print(f"The selected name is {inspector.name}")
        #if the inspectors score is no higher than five above the average score .. do this
        if inspector.score <= (averageScore() + 5) :
            notAValidNameYet = False
            sqlFunctions.incrementScoreByName(inspector.name)
            sqlFunctions.uploadMostRecentInspector(inspector.name)
            print(f"The most recently selected person is {sqlFunctions.downloadMostRecentInspector()}")
            return inspector.name
        
#this function adds an extra step to skip the last inspector(removing their point) before calling 
#the getRandomInspectorWithinReason() 
def skipTheLastInspectorFirst():
    sqlFunctions.decrementScoreByName(sqlFunctions.downloadMostRecentInspector())
    return getRandomInspectorWithinReason()

    
def randomcolor() :
    #first lets get random RGB values
    red, green, blue = random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)
    #converting the RGB values to a hexadecimal so computer can read it
    color = f'#{red:02x}{green:02x}{blue:02x}'
    return color
def averageScore() :
    everyone = sqlFunctions.fetchAllInspectors()
    score = 0
    #for every row in the inspector table, take their score and add it to the total
    for row in everyone:
        score += row[2]
    #the total divided by the number of inspectors is the average score
    score = (score / len(everyone))
    print(f"The average score is {score}")
    #let's print everyones score in the console to make sure the average makes sense
    for row in everyone:
        print(row)
    return score