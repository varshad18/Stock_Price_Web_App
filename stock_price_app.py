import yfinance as yf
import streamlit as st
import pandas as pd
import pyfolio as pf

df=pd.read_csv('Tickers.csv')
currency=df['Currencies'].dropna()
curname=df['CurrName'].dropna()
cryptocur=df['Cryptocurrencies'].dropna()
crypname=df['Cryptonames'].dropna()
mutualfunds=df['MutualFunds'].dropna()
mutualname=df['Mutualnames'].dropna()
trending=df['Trending'].dropna()
trendnames=df['Trendnames'].dropna()

html_temp = """
    <div style="background-color:#6600cc ;padding:10px;margin-bottom:10px;">
    <h1 style="color:white;text-align:center;">   Stock  Price Web Application</h1>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

st.sidebar.title("Pages")
Pages=['Trending','Mutual Funds','CryptoCurrencies','Currencies','Google','Amazon','Others']
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

if add_pages=='Trending':
    teams = st.selectbox('',trending)
    #define the ticker symbol
    tickerSymbol = teams
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='1990-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    x=int(df[df['Trending']==tickerSymbol].index.values)
    st.write("Stock price details for ",df.iloc[x]['Trendnames'])
    st.write("Open Price:")
    st.line_chart(tickerDf.Open)
    st.write("Volume of Shares:")
    st.line_chart(tickerDf.Volume)
    st.write("Closing Price:")
    st.area_chart(tickerDf.Close)

elif add_pages=='Mutual Funds':
    #define the ticker symbol
    teams = st.selectbox('',mutualfunds)
    tickerSymbol = teams

    x=int(df[df['MutualFunds']==tickerSymbol].index.values)
    st.write("Stock price details for ",df.iloc[x]['Mutualnames'])

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

elif add_pages=='Google':
    #define the ticker symbol
    tickerSymbol = 'GOOGL'
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='1990-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.write("Details for GOOGLE")
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
    st.write("Details for AMAZON")
    st.write("Open Price:")
    st.line_chart(tickerDf.Open)
    st.write("Volume of Shares:")
    st.line_chart(tickerDf.Volume)
    st.write("Closing Price:")
    st.area_chart(tickerDf.Close)
    
elif add_pages=='CryptoCurrencies':
    teams1 = st.selectbox('',cryptocur)
    tickerSymbol = teams1
    x=int(df[df['Cryptocurrencies']==tickerSymbol].index.values)
    st.write("Stock price details for ",df.iloc[x]['Cryptonames'])
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='1990-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    
    st.write("Open Price:")
    st.line_chart(tickerDf.Open)
    st.write("Volume of Shares:")
    st.line_chart(tickerDf.Volume)
    st.write("Closing Price:")
    st.area_chart(tickerDf.Close)

elif add_pages=='Currencies':
    #cur=['EURUSD=X','JPY=X','INR=X']
    teams = st.selectbox('',currency)
    tickerSymbol = teams
    
    x=int(df[df['Currencies']==tickerSymbol].index.values)
    st.write("Stock price details for ",df.iloc[x]['CurrName'])

    #st.write("Stock price details for ",tickerSymbol)
    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='1990-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    
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
