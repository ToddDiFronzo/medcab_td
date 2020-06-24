from flask import Flask, request, jsonify
from pred_request import *

app = Flask(__name__)
# FLASK_APP=main flask run

@app.route("/")
def root():
    return {"message": "Hello World"}

@app.route("/predictions", methods=['POST'])
def predict():
    request_json = request.get_json()
    user_input = request_json.get("user_input")
    pred_request = PredRequest(user_input=user_input)
    pred = pred_request.pred()
    return jsonify({"Prediction": pred})

if __name__ == "__main__":
    app.run()