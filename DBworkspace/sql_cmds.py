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
#R (read)
#code to read the song from a certain artist
#mycursor.execute("SELECT * FROM artists WHERE artist_name = 'LADY GAGA'");
#search up a song
#mycursor.execute("SELECT * FROM song WHERE track_name = 'Die For You'")
#little complex reading
#mycursor.execute("SELECT s.track_name, s.streams, a.artist_name FROM song s JOIN artists a ON s.track_name = a.track_name WHERE s.streams = ( SELECT MAX(streams) FROM Song );")

#C (create)
#add songs
#mycursor.execute("INSERT INTO song (track_name, artist_name, released_year, released_month, released_day, streams, in_spotify_playlists, in_apple_playlists) VALUES ('Fake Love', 'BTS', 2023, 11, 25, 10000, 1, 0)")
#db.commit()
#mycursor.execute("SELECT * FROM song WHERE track_name = 'Fake Love'")
#D (delete)
# delete song
#mycursor.execute("DELETE FROM song WHERE track_name = 'Fake Love' ")
#db.commit()
#mycursor.execute("SELECT * FROM song WHERE track_name = 'Fake Love'")
#result = mycursor.fetchall()

#if not result:
#    print("Song 'Fake Love' has been deleted.")
#else:
#    print("Song 'Fake Love' still exists.")

#Update (U)
#updating the number of streams
#mycursor.execute("INSERT INTO song (track_name, artist_name, released_year, released_month, released_day, streams, in_spotify_playlists, in_apple_playlists) VALUES ('Fake Love', 'BTS', 2023, 11, 25, 10000, 1, 0)")
#db.commit()
#mycursor.execute("UPDATE Song SET streams = 9 WHERE track_name = 'Fake Love'")
#db.commit()
#mycursor.execute("SELECT * FROM song WHERE track_name = 'Fake Love'")
#D (delete)
# delete song
#mycursor.execute("DELETE FROM song WHERE track_name = 'Fake Love' ")
#db.commit()
#mycursor.execute("SELECT * FROM song WHERE track_name = 'Fake Love'")
#result = mycursor.fetchall()

#if not result:
#    print("Song 'Fake Love' has been deleted.")
#else:
#    print("Song 'Fake Love' still exists.")


#output test
#for x in mycursor:
 #  print(x)
