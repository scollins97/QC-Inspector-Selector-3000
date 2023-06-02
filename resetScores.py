import sqlFunctions
keepgoing = True
while keepgoing ==True:
    password = input("Enter the password -> ")
    if password == "SonicTheHedgehog":
        sqlFunctions.resetScoresToZero()
        keepgoing = False
    else:
        print("sorry, that wasn't the right password")