#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """return hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns 'C ' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Returns 'C ' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_display(n):
    """Returns 'int ' followed by the value of the text variable"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_display(n):
    """Returns 'int ' followed by the value of the text variable"""
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def evenorodd(n):
    """Returns 'int' followed by even or odd"""
    s = ""
    if n % 2 == 0:
        s = "even"
    else:
        s = "odd"
    n = str(n)
    return render_template('6-number_odd_or_even.html', n=n, s=s)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
