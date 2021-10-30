# Project-4
____________________________________________________
## Stock Clustering and Prediction : A Machine Learning Project

____________________________________________________

![image](https://user-images.githubusercontent.com/82990618/138196855-1c949e12-f55c-4c5c-a93a-8bcd0e69da67.png)

### Contributors: 
**Vasantha Mutyala (V-MalM) / Valense Acquah-Louis (Tema-2021) / Saiyid Kazmi (saiyidmkazmi)  / Debra Potts (dschoen24)**

### Objective
* Stock market Analysis involves several non-technical aspects that are psychological or political in nature, which makes it near impossible to forecast.
We will only be doing a technical analysis to see how ML can be used as a tool in addition to non-technical studies to better predict stocks.

### Overview
#### STOCKS
Stocks are investments/ shares within a company. Companies use stocks to raise money to fund the growth of the company, products within the company or other initiatives.
By investing in a company long-term one can receive dividend or regular payments of profit made on the stock. When stocks are left to grow there is a better opportunity for the investment (stock) to grow as most companies tend to increase their profit and this in-turn means higher dividends.
Some examples of stocks are:
* Common Stock
* Preferred Stock
* Domestic Stock
* Dividend Stock
* Non-dividend Stock

Stocks time series can be grouped together when they are moving together with an underlying trend i.e., for an appropriate window of time stocks trend together.
The analysis was based on 3 indices S&P 500, NASDAQ 100 and DOW 30. 

#### CLUSTERING
Clustering is an Unsupervised Machine Learning process that splits a dataset or observations into groups that are like each other.
The clustering was performed on the datasets using K-Means and PCA on 3 different calculated features.
* Movement
* Percent Change
* Volatility

#### K-Means

K-Means is an SkLearn/ SciKit-Learn model. This model aims to group several observations / datasets into clusters (K-Clusters) where each observation within the cluster shares similarities like
* Mean
* Variance
* Patterns etc.
K-Means identifies the number of centroids in the dataset then assigns the nearest cluster where the centroids remain as small as possible.

![Elbow curve 2021-10-30 183509](https://user-images.githubusercontent.com/82990618/139561275-70072bc9-a4d7-4903-8d27-c714cd93df98.png)

#### MOVEMENT

Movement is a measure of identifying the trend direction of a stock and this helps identify the resistance level of the stock and also determine its support. It is measured by determining the average changes in open and close price of the stock to help determine if the stock is going in an uptrend (rising movement) or downtrend (declining movement). 

![movement 2021-10-30 184612](https://user-images.githubusercontent.com/82990618/139561359-90885015-fd48-4e9c-a0ee-6246f1de85e5.png)

 From the image of the various indices S&P500 and NASDAQ100 can be grouped into 5 clusters to represent the various stocks that are moving in the same direction whereas DOW30 has 3 clusters.
 
 #### TABLEU
 Within Tableau, we created two separate  Treemap charts for each of our indices - S&P 500, Nasdaq 100 and Dow 30.  
Our first Treemap chart is based on Market Movement (the change in share prices based on supply & demand) which we categorized by color diversity for each cluster within the index.  
For this first Treemap chart, we used the ticker name of each stock and the attribute Company as our labels, the attribute Cluster as our color diversity and included the attribute Movement as the size of each branch.  On our webpage, when hovering over a specific branch on the webpage, it will show the stock symbol, company name and show what cluster that specific stock belongs to.
Our second Treemap chart is based on percent change (returns) and volatility which we also categorized by color diversity for each cluster within the index.  Percent change measures the difference of closing price from the beginning of a time period to the end of a time period.  We chose a time period of 2 years.  Volatility in this Treemap chart is the reflection of the degree to which price moves.  We calculated the volatility using Standard Deviation.
For this second Treemap chart, we used the Stock name as our label, the attribute Cluster as our color diversity and included the attribute Returns as the size of each branch.  Within our website, when hovering over a branch, it will list the stock by symbol & company name, give you the numbered cluster to which it belongs and list the return percentage.


### WEBSITE
![homepage 2021-10-30 175633](https://user-images.githubusercontent.com/82990618/139560800-8af57ca8-d211-430a-8b13-6dc5829fd1f4.png)
### HOME PAGE
Our webpage was designed using a template from bootstrap and customizing it to suit our project. Six company logos and a list of daily stocks scrolling at the bottom of the homepage, this was obtained by using MacroAxis widget. On the top right corner of the page are 3 tabs 
* Home
* Clusters (with a drop down menu of “Clusters Explained” and “Outliers”)
* Predict
 #### 'Clusters' Tab
 The first item on the drop down menu directs you to the clusters page




