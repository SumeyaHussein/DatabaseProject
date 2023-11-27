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

        # Fetch results
        #result = mycursor.fetchall()

        # If you expect to retrieve column names, you can fetch them like this:
        #column_names = [desc[0] for desc in mycursor.description]

        # Assuming you want to return results as JSON
        #if result:
        #    data = []
        #    for row in result:
        #        data.append(dict(zip(column_names, row)))
        #    return jsonify({'result': data})
        #else:
        #    return jsonify({'result': 'No data found'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)