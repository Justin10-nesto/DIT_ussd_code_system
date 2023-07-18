import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/ussd", methods = ['POST'])
def handle_json():
    data = request.json
    print(data.get('name'))
    print(data.get('age'))
    return data

if __name__ == '__main__':
    app.run(debug=True)