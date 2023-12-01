import sqlite3
import pandas as pd

df = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')
df.columns = df.columns.str.strip()
connection = sqlite3.connect('spotify-2023.db')


cursor = connection.cursor()


sql_command = "CREATE TABLE Artist (artist_name VARCHAR(255) PRIMARY KEY,track_name VARCHAR(255));"
# Execute the SQL command
cursor.execute(sql_command)
#print ("connected to databse") #uncomment to test connection
# Commit changes and close the connection
connection.commit()

select_query = "SELECT * FROM Artist;"
cursor.execute(select_query)
table_contents = cursor.fetchall()
for row in table_contents:
    print(row)  # Display each row of the table

connection.close()
