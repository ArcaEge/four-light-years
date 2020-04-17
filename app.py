from flask import Flask, render_template, send_file
import requests

app = Flask(__name__)

imgweb = requests.get('https://api.nasa.gov/planetary/apod?api_key=lHQ3b7vfBGmXtllBqabTiGtuLoEcVgC20gAlnpyF')
img = imgweb.json()
launches = requests.get('https://spacelaunchnow.me/api/3.3.0/launch/upcoming/?format=json&limit=5')
launches = launches.json()


@app.route('/')
def home():
    return render_template('index.html', img=img, launch=launches)
