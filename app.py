from flask import Flask, request, jsonify
from .pred_request import *
import logging
import requests

app = Flask(__name__)
# FLASK_APP=app flask run

# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s - %(levelname)s - %(message)s")

@app.route("/")
def root():
    return {"message": "Hello World"}

@app.route("/predictions", methods=['POST'])
def predict():
    """[summary]

    Returns
    -------
    [type]
        [description]
    """
    request_json = request.get_json()
    user_id = request_json["user_id"]
    user_input = request_json["user_input"]
    pred_request = PredRequest(user_input=user_input)
    pred = pred_request.pred()

    url = "https://cannedmedical.herokuapp.com/recommendation/search"
    logging.info(url)
    payload = {"user_id": user_id,
                "Prediction": pred}
    logging.info(payload)
    res = requests.post(url, json=payload)
    logging.info("status_code: " + str(res.status_code))
    print("status_code: " + str(res.status_code))

    return jsonify({"user_id": user_id,
                    "Prediction": pred})

if __name__ == "__main__":
    app.run()