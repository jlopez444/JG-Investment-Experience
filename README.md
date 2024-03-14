# JG Investment Experience
Welcome to the "JG Investment Experience"!  This is my first full-stack program venture!  In this project, I created a program using the Streamlit framework, which allows users to input a stock ticker, view the latest stock price, visualize dividends and closing prices over time, and perform buy/sell operations.  This program is intended to inform the customer of crucial data before executing the buy/sell operation.  I used alpacas api and yfinance api to extract live data using the stock ticker as a global variable called symbol.  I then use vertain functions from alpacas api to call on specific data such as latest price, dividens, and closing prices.  Then, I used certain streamlit functions to visualize those result.  Finally, I connected my personal alpacas paper trading account to demonstrate that the buy/sell operations were successfully processed.  Enjoy!

## Dependencies
The imports I use were
* import streamlit as st
* import warnings
* warnings.filterwarnings("ignore")
* from dataclasses import dataclass
* from typing import Any, List
* #from web3 import Web3
* import alpaca_trade_api as tradeapi
* from alpaca.data.historical import StockHistoricalDataClient
* from alpaca.data.requests import StockLatestQuoteRequest# Create stock historical data client
* from alpaca.trading.client import TradingClient
* from alpaca.trading.requests import GetAssetsRequest, MarketOrderRequest, GetOrdersRequest
* from alpaca.trading.enums import AssetClass, OrderSide, TimeInForce, OrderStatus
* import alpaca_trade_api as tradeapi
* #w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
* import requests
* import yfinance as yf
* import datetime as dt
* import pandas as pd
* import hvplot.pandas
