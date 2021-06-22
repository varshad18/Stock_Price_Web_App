import yfinance as yf
import streamlit as st
import pandas_datareader
import pandas as pd
from pandas_datareader import data
import pyfolio as pf

html_temp = """
    <div style="background-color:#6600cc ;padding:10px;margin-bottom:10px;">
    <h1 style="color:white;text-align:center;">   Stock  Price Web Application</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

st.sidebar.title("Pages")
Pages=['Google','Amazon','Bitcoin USD','Currencies','Others']
add_pages = st.sidebar.selectbox('', Pages)
st.sidebar.title("Note:")
html_temp6 = """
<ul>
<p style="color:#000066;">
<li>Few tickers are mentioned in the dropdown; In order to see details of other tickers goto the Others Page.</li>
<li>The ticker symbols can be found <a href="https://finance.yahoo.com/lookup/"> here </a></li>
</p>
</ul>
<br>
<h3>Developed by:<br></h3>
<p style="color:#6600cc;">
Varshashree D<br></p>
Github: <a href="https://github.com/varshad18">https://github.com/varshad18</a> <br>
"""
st.sidebar.markdown(html_temp6, unsafe_allow_html=True)
# Set the start and end date
start_date = '1990-05-31'
end_date = '2020-05-31'
if add_pages=='Google':
    # https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
    #define the ticker symbol
    tickerSymbol = 'GOOGL'
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='1990-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.write("Details for ",tickerSymbol)
    st.write("Open Price:")
    st.line_chart(tickerDf.Open)
    st.write("Volume of Shares:")
    st.line_chart(tickerDf.Volume)
    st.write("Closing Price:")
    st.area_chart(tickerDf.Close)





elif add_pages=='Amazon':
    tickerSymbol = 'AMZN'
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='1990-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    st.write("Details for ",tickerSymbol)
    st.write("Open Price:")
    st.line_chart(tickerDf.Open)
    st.write("Volume of Shares:")
    st.line_chart(tickerDf.Volume)
    st.write("Closing Price:")
    st.area_chart(tickerDf.Close)
elif add_pages=='Bitcoin USD':
    tickerSymbol = 'BTC-USD'
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='1990-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    st.write("Details for ",tickerSymbol)
    st.write("Open Price:")
    st.line_chart(tickerDf.Open)
    st.write("Volume of Shares:")
    st.line_chart(tickerDf.Volume)
    st.write("Closing Price:")
    st.area_chart(tickerDf.Close)
elif add_pages=='Currencies':
    cur=['EURUSD=X','JPY=X']
    teams = st.selectbox('',cur)
    st.write("Stock price details for ")
    tickerSymbol = teams
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='1990-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    st.write("Details for ",tickerSymbol)
    st.write("Open Price:")
    st.line_chart(tickerDf.Open)
    st.write("Volume of Shares:")
    st.line_chart(tickerDf.Volume)
    st.write("Closing Price:")
    st.area_chart(tickerDf.Close)
elif add_pages=='Others':
    user_input = st.text_input("Enter Ticker Symbol", 'AAPL')
    tickerSymbol = user_input
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='1990-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    st.write("Details for ",tickerSymbol)
    st.write("Open Price:")
    st.line_chart(tickerDf.Open)
    st.write("Volume of Shares:")
    st.line_chart(tickerDf.Volume)
    st.write("Closing Price:")
    st.area_chart(tickerDf.Close)