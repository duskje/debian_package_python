from flask import Flask


app = Flask(__name__)

@app.route('/ping')
def hello_world():
    return "pong"

app.run()
