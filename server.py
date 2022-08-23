"""Greeting Flask app."""

from random import choice
import re

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
      <html>Hi! This is the home page.
      <head>
        <title></title>
      </head>
      <body>
        <a href="/hello">Link</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="radio" name="compliments" value="sweet" id="sweet">
          <label for="sweet">sweet</label>
          <input type="radio" name="compliments" value="funny" id="funny">
          <label for="funny">funny</label>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/diss')
def say_insult():

    return """
      <!doctype html>
    <html>
      <head>
        <title>You are the worst!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="radio" name="insults" value="lazy" id="lazy">
          <label for="lazy">lazy</label>
          <input type="radio" name="insults" value="boring" id="boring">
          <label for="boring">boring</label>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
  
  """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    # person is the dict key, the val is the name
    # they typed on form
    # assign value to var player
    player = request.args.get("person")

    compliment = request.args.get("compliments")

    insult = request.args.get("insults")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
