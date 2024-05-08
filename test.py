from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get_string')
def get_string():
    return 'This is the string you want to return.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7123)