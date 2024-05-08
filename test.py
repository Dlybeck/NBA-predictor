from flask import Flask

app = Flask(__name__)

@app.route('/get_string')
def get_string():
    return 'This is the string you want to return.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)