#!/usr/bin/python3
# flask app

from flask import Flask
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hello_world():
    # prints hbnb
    return "HBNB!"


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)