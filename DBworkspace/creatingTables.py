import mysql.connector
import pandas as pd 

#empdata = pd.read_csv('C:\Users\Thinking1\vsc_workspace\spotify-2023.csv', index_col=False, delimiter = ',')
#empdata.head()

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd="root",
    database= "spotify-2023"
    )
mycursor = db.cursor()
#mycursor.execute("SELECT * FROM spotify2023")
#
# Create Table
#create_table_query = """
#CREATE TABLE artists (
#    artist_name VARCHAR(255),
#    track_name VARCHAR(255)
#)
#"""
#mycursor.execute(create_table_query)

# Insert Data
#insert_data_query = """
#INSERT INTO artists (artist_name, track_name)
#SELECT `artist(s)_name`, `track_name` FROM spotify2023
#"""
#mycursor.execute(insert_data_query)

# Commit the changes if using transactions
#db.commit()
#TESTING artists
#mycursor.execute("SELECT * FROM artists")

#output test
#for x in mycursor:
#    print(x)
