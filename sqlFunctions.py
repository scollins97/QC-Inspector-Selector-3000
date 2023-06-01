#this program handles any SQL related queries
import sqlite3

def selectRandomInspector():
    #create a connection to the database
    conn = sqlite3.connect("Python\QC-Inspector-Selector\QCdb.db")
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
    conn = sqlite3.connect("Python\QC-Inspector-Selector\QCdb.db")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inspectors")
    results = cursor.fetchall()
    conn.close()
    return results

def incrementScoreByName(theirName) :
    #create a connection to the database
    conn = sqlite3.connect("Python\QC-Inspector-Selector\QCdb.db")
    #create a cursor object. this allows queries to be made
    cursor = conn.cursor()
    cursor.execute(f"UPDATE inspectors SET score = score + 1 WHERE name = '{theirName}'")
    conn.commit() #committing the changes to the database
    conn.close()
    return