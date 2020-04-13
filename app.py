from flask import Flask, render_template
import requests

app = Flask(__name__)

imgweb = requests.get('https://api.nasa.gov/planetary/apod?api_key=lHQ3b7vfBGmXtllBqabTiGtuLoEcVgC20gAlnpyF')
img = imgweb.json()


@app.route('/')
def home():
    return render_template('index.html', img=img)
