import json
import pylyrics3
from flask import Flask, render_template
import markovify


# app = Flask(__name__, static_url_path='/static')
def getlyrics():
    blinklyrics = pylyrics3.get_artist_lyrics('Blink-182')
    for k, v in blinklyrics.items():
      print(v)

    with open('blinklyrics.txt', 'w') as file:
         file.write(json.dumps(blinklyrics))
    with open("blinklyric.txt", 'w') as f:
        for value in blinklyrics.items():
            f.write(value)

    # @app.route("/")
# def index():
#     ewords = smithize()
#     while ewords is None:
#         ewords = smithize()
#     return render_template("index.html", words=ewords)
getlyrics()
