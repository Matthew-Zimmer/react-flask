# Create an endpoint "/movies" which returns an list of movies
# A movie is record of the following keys (id, name, rating, genre, duration)
# You can return hardcoded data no database required for this

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return jsonify({ "msg": "Hello World" })

if __name__ == '__main__':
    app.run()