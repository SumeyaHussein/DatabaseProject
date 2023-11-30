import mysql.connector
import pandas as pd 
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
#empdata = pd.read_csv('C:\Users\Thinking1\vsc_workspace\spotify-2023.csv', index_col=False, delimiter = ',')
#empdata.head()

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd="root",
    database= "spotify-2023"
    )
mycursor = db.cursor()
#print("connected")

@app.route('/')
def welcome():
    return render_template('welcomepage.html')

# Route for running SQL queries
@app.route('/testWeb')
def testWeb():
    return render_template('testWeb.html')  # You'll need to create this HTML file

# Route for creating a playlist
#@app.route('/create_playlist')
#def create_playlist():
#    return render_template('create_playlist.html')  # You'll need to create this HTML file

@app.route('/playlist')
#def create_playlist():
def playlist():
    return render_template('playlist.html')  # You'll need to create this HTML file

@app.route('/ownSong')
#def create_playlist():
def own_song():
    return render_template('ownSong.html')  # You'll need to create this HTML file

@app.route('/create_playlist')
#def create_playlist():
def create_playlist():
    return render_template('create_playlist.html')  # You'll need to create this HTML file
    
@app.route('/likedsongs')
def likedsongs():
    return render_template('likedsongs.html')  # You'll need to create this HTML file
    

# Your existing SQL query handling route
###
@app.route('/add_song', methods=['POST'])
def add_song():
    try:
        artist_name = request.form.get('artist_name')
        track_name = request.form.get('track_name')
        # Get other song attributes similarly

        # Execute SQL query to add the song to the playlist
        query = f"INSERT INTO playlist (artist_name, track_name) VALUES ('{artist_name}', '{track_name}')"
        mycursor.execute(query)
        db.commit()  # Commit chan
        # Receive song details from the request
        #track_name = request.form.get('artist_name track_name')
        # Get other song attributes similarly

        # Execute SQL query to add the song to the playlist
        #query = f"INSERT INTO playlist (artist_name, track_name) VALUES ('{track_name}')"
        #mycursor.execute(query)
        #db.commit()  # Commit changes to the database

        return render_template('ownSong.html')

    except Exception as e:
        return jsonify({'error': str(e)})

# Route to get a song recommendation
#@app.route('/get_recommendation', methods=['GET'])
#def get_recommendation():
 #   try:
        # Your logic to generate a song recommendation goes here
        # This could involve SQL queries or other methods to fetch a recommended song

        # For example, a simple SQL query to get a random song from your database
  #      query = "SELECT track_name FROM song ORDER BY RAND() LIMIT 1" #modify so that based on the user liking
        #of each feild it reflects a playlist from that
   #     mycursor.execute(query)
    #    result = mycursor.fetchone()

        # You can process the recommendation and pass it to the frontend
     #   recommendation = result[0] if result else None

      #  return jsonify({'recommendation': recommendation})
@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    try:
        # Get user inputs for song attributes
        danceability = request.form.get('danceability')
        valence = request.form.get('valence')
        energy = request.form.get('energy')
        acousticness = request.form.get('acousticness')
        instrumentalness = request.form.get('instrumentalness')
        liveness = request.form.get('liveness')
        speechiness = request.form.get('speechiness')
        # ...and so on for other attributes
        danceability = float(danceability) if danceability is not None else 0.0
        valence = float(valence) if valence is not None else 0.0
        energy = float(energy) if energy is not None else 0.0
        acousticness = float(acousticness) if acousticness is not None else 0.0
        instrumentalness = float(instrumentalness) if instrumentalness is not None else 0.0
        liveness = float(liveness) if liveness is not None else 0.0
        speechiness = float(speechiness) if speechiness is not None else 0.0

        # Construct the SQL query based on user inputs
        query = f"""
            SELECT track_name,
            SQRT(POWER(danceability - {danceability}, 2) + 
                 POWER(valence - {valence}, 2) + 
                 POWER(energy - {energy}, 2) + 
                 POWER(acousticness - {acousticness}, 2) +
                 POWER(instrumentalness - {instrumentalness}, 2) +
                 POWER(liveness - {liveness}, 2) + 
                 POWER(speechiness - {speechiness}, 2)) AS distance
            FROM song_attributes
            ORDER BY distance
            LIMIT 10
        """

        mycursor.execute(query)
        results = mycursor.fetchall()

        # Process results and send to frontend
        data = [{'track_name': row[0], 'similarity': row[1]} for row in results]
        return render_template('create_playlist.html', recommendations=data)
    
    
    except Exception as e:
        return jsonify({'error': str(e)})




@app.route('/query', methods=['POST'])
def run_query():
    try:
        # Receive SQL query from request
        query = request.json.get('query')
        
        # Execute SQL query
        mycursor.execute(query)

        # For SELECT queries
        if mycursor.description:
            column_names = [desc[0] for desc in mycursor.description]
            result = mycursor.fetchall()
            data = []
            for row in result:
                data.append(dict(zip(column_names, row)))
            return jsonify({'result': data})
        else:
            # For INSERT, UPDATE, DELETE queries
            db.commit()  # Commit changes to the database
            return jsonify({'result': 'Query executed successfully'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
