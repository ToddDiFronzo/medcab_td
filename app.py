from flask import Flask
from pred_request import *

app = Flask(__name__)
# FLASK_APP=main flask run

@app.route("/")
def root():
    return {"message": "Hello World"}

@app.route("/predictions/", methods=['POST'])
def predict(pred_request: PredRequest):
    rec_strains = pred_request.pred()
    return {"Recommended Strains": rec_strains}

if __name__ == "__main__":
    app.run()