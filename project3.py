import streamlit as st
import warnings
warnings.filterwarnings("ignore")
from dataclasses import dataclass
from typing import Any, List
#from web3 import Web3
import alpaca_trade_api as tradeapi
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest# Create stock historical data client
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest, MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import AssetClass, OrderSide, TimeInForce, OrderStatus
import alpaca_trade_api as tradeapi
#w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
import requests
import yfinance as yf
import datetime as dt
import pandas as pd
import hvplot.pandas
#Program Title
st.title("JG Investment Interface")

#Global Variables
symbol = st.text_input("Put your stock ticker here")
stock = yf.Ticker(symbol)
dividends = stock.dividends

# Streamlit app
def main():

    
    # Button to print latest value
    if st.button('Push to find latest value'):
        client = StockHistoricalDataClient('PKYYGDW5MS43IU3HC95D', 'Vq9DYwiETpYXE2KOrR171qFd9WA3LAj8biUetXfx')# Create request
        multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=[symbol])
        latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)
        latest_ask_price = latest_multisymbol_quotes[symbol].ask_price
        print(latest_ask_price)
        st.write(latest_ask_price)
    start_date = st.date_input("Enter start date")
    end_date = st.date_input("Enter end date", value=dt.date.today())

    # Button to print Dividends and Closing Prices
    if st.button('Push for Dividends and Closing Prices!'):
  
    # Dividend Values   
        if not dividends.empty:
         # Convert index to hashable type
            dividends.index = pd.to_datetime(dividends.index)
        # Plot dividends using st.line_chart()
            st.write("## Dividends Over Time")
            st.line_chart(dividends)
        else:
            st.write("No dividend data available for this stock.")
            print(stock.history())
            stock.actions
    
    #closing values
        historical_data = stock.history(start=start_date, end=end_date)
        if not historical_data.empty:
        # Extract close prices
            close_prices = historical_data['Close']
            st.write("## Closing Prices Over Time")
            st.write(f"Close prices for {symbol} from {start_date} to {end_date}:")
            st.line_chart(close_prices)
        else:
            st.write(f"No historical data available for {symbol}.")

if __name__ == '__main__':
    main()

# Buy/Sell Operations
qty=1

select_option=st.selectbox("Buy or Sell",["Buy","Sell"])

confirm=st.button("Confirm")

api_key = "PKYYGDW5MS43IU3HC95D"
api_secret = "Vq9DYwiETpYXE2KOrR171qFd9WA3LAj8biUetXfx"

trading_client = TradingClient(api_key, api_secret, paper=True)

if select_option == "Buy" and confirm:
    market_order_data = MarketOrderRequest(
                   symbol=(symbol),  
                   qty=qty,  
                   side=OrderSide.BUY,  
                   time_in_force=TimeInForce.DAY  
                   )
    market_order = trading_client.submit_order(
    order_data=market_order_data
    )
    st.write("You have successfully bought a stock")
    st.balloons()
    st.write("Thank you for choosing the JG Investment Experience!")
elif select_option == "Sell" and confirm:
    market_order_data = MarketOrderRequest(
                   symbol=(symbol),  
                   qty=qty,  
                   side=OrderSide.SELL,  
                   time_in_force=TimeInForce.DAY  
                   )
    market_order = trading_client.submit_order(
    order_data=market_order_data
    )
    st.write("You have successfully sold a stock")
    st.balloons()
    st.write("Thank you for choosing the JG Investment Experience!")

