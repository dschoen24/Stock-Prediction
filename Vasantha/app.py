from flask import Flask, render_template, redirect, request, url_for
import json
from flask.json import jsonify
from sqlalchemy import create_engine
import pandas as pd
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["GET", "POST"])
def pred():
    
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static\js", "tickers.json")
    data = json.load(open(json_url))
    print(json_url)
    

    selected_stock="TSLA"
    if request.method == "POST":
        selected_stock = request.form["selDataset"]
        
    return render_template("predict.html", data=data, selected_stock=selected_stock) 

        


if __name__ == "__main__":
    app.run(debug=True, port=5000,use_reloader=True)