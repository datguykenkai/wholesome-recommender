from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

from getInfo import get_url, get_number, get_doujin

@app.route('/')
def index():

    url = get_url()
    num = get_number(url)
    info = get_doujin(num)

    data = {"url": url,
            "number": num,
            "info": info}
    return data

if __name__ == "__main__":
    app.run()

"""
$env:FLASK_APP="flaskAPI.py"
$env:FLASK_ENV="development"
flask run
"""