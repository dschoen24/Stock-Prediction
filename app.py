from flask import Flask, render_template, redirect, request, url_for
import json
from flask.json import jsonify
import os

import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import pandas_datareader as pdr
from datetime import datetime, timedelta



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/stocks")
def stocks():
    return render_template('stocks.html')

@app.route("/stocksP")
def stocksP():
    return render_template('stocks_2.html')    

@app.route("/team")
def team():
    return render_template('team.html')    

@app.route("/predict", methods=["GET", "POST"])
def pred():
    
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static\js", "tickers.json")
    data = json.load(open(json_url))
    data = sorted(data, key = lambda i: i['ticker'])
    
    selected_ticker ="SBUX"
    selected_stock = "Starbucks Corporation"
    img_png = "Images/TSLA.png"
    if request.method == "POST":
        selected_ticker = request.form["selDataset"]
        # img_png = "Images/"+selected_ticker+".png"
        for x in data:
            if(selected_ticker == x['ticker']):
                selected_stock = x['stock']

    if (selected_ticker != ""):
        #Get the stock
        ticker = selected_ticker
        today = datetime.today()
        model_file_name = "Model_"+selected_ticker+".h5"

        # for predictions add 100 extra days to make sure it has more than ts_points to make up for missing days (weekends and holidays)
        # while calling thos model we will have to pass the excat number of ts_points as that were used while training the model
        ts_points = 120
        fetch_days = ts_points + 100    

        sd =  today - timedelta(days=fetch_days)
        sd = sd.strftime('%Y-%m-%d')

        ed = today.strftime('%Y-%m-%d')
        ed

        next_day = (today + timedelta(days=1) ).strftime('%Y-%m-%d')
        # next_day
        # get the quote
        quote = pdr.DataReader(ticker, data_source="yahoo", start=sd, end=ed)
        new_df = quote.filter(['Close'])
        last_n_days = ts_points
        last_n_days_arr = new_df[-last_n_days:].values 

        scaler = MinMaxScaler(feature_range=(0,1))
        last_n_days_scaled = scaler.fit_transform(last_n_days_arr)
        X_test = []
        X_test.append(last_n_days_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test,(X_test.shape[0], X_test.shape[1],1))
        
        ##########################loading saved model ###############################
        new_model = tf.keras.models.load_model('assets/'+model_file_name)
        nmpred_price = new_model.predict(X_test)
        nmpred_price = scaler.inverse_transform(nmpred_price)
        nmpred_price = nmpred_price[0][0]
        #print(f"Predicted Closing price for '{selected_stock}' on {next_day} is {nmpred_price:.4f}")

        d1 = today - timedelta(days=8)
        d1 = d1.strftime('%Y-%m-%d')

        recent_his = pdr.DataReader(ticker, data_source="yahoo", start=d1)
        recent_his = recent_his.reset_index()
        recent_his = recent_his.to_html(index=False)
        recent_his = recent_his.replace('\n','')
        recent_his = recent_his.replace('class="dataframe"','class="table tablipede-str"')
        recent_his = recent_his.replace('<thead>    <tr style="text-align: right;">      <th>0</th>      <th>1</th>    </tr>  </thead>','')
        
        

    return render_template("predict.html", data=data, selected_ticker=selected_ticker, \
            selected_stock=selected_stock, nmpred_price=nmpred_price, recent_his=recent_his, today=today) 

        
if __name__ == "__main__":
    app.run(debug=True, port=5000,use_reloader=False)