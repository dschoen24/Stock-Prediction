from flask import Flask, render_template, redirect, request
import json
from flask.json import jsonify
from sqlalchemy import create_engine
import pandas as pd
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000,use_reloader=False)