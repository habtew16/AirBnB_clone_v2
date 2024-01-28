#!/usr/bin/python3
"""
starts flask with python text
"""
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    return 'C ' + text.replace("_", ' ')


@app.route('/python/')
@app.route('/python/<text>')
def ptext(text='is cool'):
    return 'Python {}'.format(text.replace("_", ' '))


@app.route('/number/<int:n>')
def is_number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_even_odd(n):
    text = ''
    if n % 2 == 0:
        text = 'even'
    else:
        text = 'odd'

    return render_template('6-number_odd_or_even.html', number=n, name=text)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
