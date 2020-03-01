from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from places_api import finder

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify("Hello to our API.")

@app.route('/atms/<location>', methods=['GET'])
def atm_near_me(location):
    return jsonify(finder("atms near "+location))


@app.route('/branches/<bank_name>/<location>', methods=['GET'])
def atm_near_me(bank_name, location):
    return jsonify(finder(bank_name+" branches near "+location))

@app.route('/rec-personal-accounts/<spec>')
def rec_accounts(spec):
    if spec == "Student":
        pass
    elif spec == "Graduate":
        pass
    elif spec == "Saver":
        pass
    elif spec == "Overdraft":
        pass
    else:
        pass

@app.route('/bank-offers/<bank_name>', methods=['GET'])
def bank_offerings(bank_name):
    pass


if __name__ == "__main__":
    app.run(debug=True)
