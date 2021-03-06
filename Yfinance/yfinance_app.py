import yfinance as yf
import streamlit as st
import pandas as pd

st.write('''
*simple stock price app

*shown are the stock closing price and volume of Apple!

''')
#define ticker symbol
tickerSymbol = 'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-7-21', end='2021-7-21')

# Open      High        Low        Close       Volume       Dividends       Stock      Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)