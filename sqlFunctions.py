#this program handles any SQL related queries
import sqlite3
import os

#these next few steps are so that if this is moved it can still find the database
# Get the path to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Specify the database file name
db_file = "QCdb.db"
# Construct the full path to the database file
path = os.path.join(current_dir, db_file)


def selectRandomInspector():
    #create a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inspectors ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    print(row)
    #close the connection
    conn.close()
    return row
#returns all the inspector rows from the database
def fetchAllInspectors():
    #create a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inspectors")
    results = cursor.fetchall()
    conn.close()
    return results
#adds a point to the given names score
def incrementScoreByName(theirName) :
    #ceate a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute(f"UPDATE inspectors SET score = score + 1 WHERE name = '{theirName}'")
    conn.commit() #committing the changes to the database
    conn.close()
    return
#removes one point from the Inspectors name given score
def decrementScoreByName(theName):
    #ceate a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute(f"UPDATE inspectors SET score = score - 1 WHERE name = '{theName}'")
    conn.commit() #committing the changes to the database
    conn.close()
    return

#this function will save the name of the most recent inspector chosen into the data base. this will become
#important later if an inspector needs to be skipped. 
def uploadMostRecentInspector(aName):
    #ceate a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute(f"UPDATE recentSelection SET name = '{aName}'")
    conn.commit()#commiting the changes just made
    return
def downloadMostRecentInspector():
    #ceate a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recentSelection")
    row = cursor.fetchone()
    inspector = row[0]
    return inspector
#this resets everyones scores to zero
def resetScoresToZero() :
    #ceate a connection to the database
    conn = sqlite3.connect(f"{path}")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    #execute the SQL query
    cursor.execute("UPDATE inspectors SET score = 0")
    #commit changes to database
    conn.commit()
    #close the connection
    conn.close()
    return