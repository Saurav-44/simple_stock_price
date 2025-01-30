import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

This app displays the **closing price**, **volume** metrics for the selected stock.

""")

# User input for stock ticker symbol
tickerSymbol = st.text_input("Enter Stock Ticker Symbol", "").strip()

# User input for date range
start_date = st.date_input("Start Date", value=pd.to_datetime("2010-05-31"))
end_date = st.date_input("End Date", value=pd.to_datetime("2020-05-31"))

# Check if the user has entered a ticker symbol
if tickerSymbol:
    try:
        # Get data on the selected ticker
        tickerData = yf.Ticker(tickerSymbol)

        # Get historical prices for the selected ticker and date range
        tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

        # Check if data is available for the selected ticker
        if not tickerDf.empty:
            # Display closing price
            st.write("""
            ## Closing Price
            """)
            st.line_chart(tickerDf.Close)

            # Display volume
            st.write("""
            ## Volume
            """)
            st.line_chart(tickerDf.Volume)

        else:
            st.warning(f"No data available for the ticker symbol: {tickerSymbol}. Please enter a valid ticker.")
    except Exception as e:
        st.error(f"An error occurred: {e}. Please check the ticker symbol and try again.")
else:
    st.info("Please enter a stock ticker symbol to view the data.")
