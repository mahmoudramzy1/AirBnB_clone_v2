#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """return hbnb"""
    return 'HBNB'


@app.route('/C/<text>', strict_slashes=False)
def show_c(text):
    """Returns 'C ' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
