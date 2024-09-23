import talib
import yfinance as yf
from datetime import datetime

# Define the currency pair and timeframe
symbol = "CHFJPY=X"  # CHF/JPY currency pair
interval = "1m"  # 1-minute timeframe

# Fetch live data from Yahoo Finance
data = yf.download(symbol, period="1d", interval=interval)

# Extract closing prices from the live data
prices = data["Close"].values

# Calculate the indicators based on live data
sma_short = talib.SMA(prices, timeperiod=5)  # Short-term moving average
sma_long = talib.SMA(prices, timeperiod=10)  # Long-term moving average

rsi = talib.RSI(prices, timeperiod=14)  # RSI

upper_band, middle_band, lower_band = talib.BBANDS(prices, timeperiod=20)  # Bollinger Bands

macd_line, signal_line, _ = talib.MACD(prices)  # MACD

slowk, slowd = talib.STOCH(prices, prices, prices)  # Stochastic Oscillator

# Generate signals based on the indicators
buy_signal = (sma_short > sma_long) & (rsi < 30) & (prices < lower_band)
sell_signal = (sma_short < sma_long) & (rsi > 70) & (prices > upper_band)

# Print the signals
current_index = len(prices) - 1
print("Buy Signal:", buy_signal[current_index])
print("Sell Signal:", sell_signal[current_index])
