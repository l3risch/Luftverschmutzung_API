#!/bin/python

from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import requests
import os


project_root_dir = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)
CORS(app)
base_url = "https://api.waqi.info/feed/"
api_token = os.getenv('API_TOKEN')


@app.route("/getAirQuality", methods=['GET'])
def get_air_quality():
    city = request.args['city']
    response = requests.get(base_url + city + "/?token=" + api_token)
    data = response.json()
    return jsonify(data)


app.run(host="0.0.0.0", port=5000)
