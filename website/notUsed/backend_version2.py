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
@app.route('/create_playlist')
def create_playlist():
    return render_template('create_playlist.html')  # You'll need to create this HTML file

# Your existing SQL query handling route


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
