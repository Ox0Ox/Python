import pandas as pd
import numpy as np
import yfinance as yf
import talib

# Define the currency pair and parameters
symbol = 'USDJPY=X'  # Example: USD/JPY currency pair
short_window = 50  # Short moving average window
long_window = 200  # Long moving average window
rsi_threshold = 30  # RSI oversold threshold

# Function to calculate moving averages and RSI
def calculate_indicators(data):
    data['SMA_short'] = data['Close'].rolling(short_window).mean()
    data['SMA_long'] = data['Close'].rolling(long_window).mean()
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    return data

# Function to generate trading signals
def generate_signals(data):
    data['Signal'] = np.where(
        (data['SMA_short'] > data['SMA_long']) & (data['RSI'] > rsi_threshold), 1,
        np.where((data['SMA_short'] < data['SMA_long']) & (data['RSI'] < 100 - rsi_threshold), -1, 0)
    )
    data['Position'] = data['Signal'].shift()
    return data

# Main trading loop
while True:
    # Fetch live price data from Yahoo Finance API
    data = yf.download(symbol, period='1d', interval='1m')

    # Calculate indicators and generate signals
    data = calculate_indicators(data)
    signals = generate_signals(data)

    # Get the most recent signal
    latest_signal = signals['Signal'].iloc[-1]

    # Place trades based on the signal
    if latest_signal == 1:
        # Place buy order
        print("Buy signal generated for", symbol)
        # Implement your trading execution code here
    elif latest_signal == -1:
        # Place sell order
        print("Sell signal generated for", symbol)
        # Implement your trading execution code here

    # Wait for the next data update
    # Implement the necessary sleep time here, such as time.sleep(60) for 1 minute interval
