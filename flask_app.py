from flask import Flask, request, jsonify
from flask_cors import CORS
from places_api import finder

app = Flask(__name__)
CORS(app)

# BASE_URL = https://munshi-ji.herokuapp.com

@app.route('/', methods=['GET'])
def index():
    return jsonify("Hello to our API.")

# /atms?loc=address+string
@app.route('/atms', methods=['GET'])
def atm_near_me():
    location = request.args.get('loc')
    return jsonify(finder("atms near "+location))

# /branches/<bank-name>?loc=address+string
@app.route('/branches/<bank_name>', methods=['GET'])
def branch_near_me(bank_name):
    location = request.args.get('loc')
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
