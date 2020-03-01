from flask import Flask, request, jsonify
import requests
from places_api import finder

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify("Hello to our API.")

@app.route('/atm')
def atm_near_me():
    return jsonify(finder("atms near me"))

if __name__ == "__main__":
    app.run(debug=True)