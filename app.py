import json
import pylyrics3
from flask import Flask, render_template
import markovify
from read import smithize

app = Flask(__name__, static_url_path='/static')
def getlyrics():
    esmith = pylyrics3.get_artist_lyrics('Elliott Smith')
    for k, v in esmith.items():
      print(v)

    with open('file.txt', 'w') as file:
         file.write(json.dumps(esmith))

@app.route("/")
def index():
    ewords = smithize()
    while ewords is None:
        ewords = smithize()
    return render_template("index.html", words=ewords)

if __name__ == '__main__':
    app.run(debug=True)
