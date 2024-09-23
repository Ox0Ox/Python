import talib
import yfinance as yf
from datetime import datetime, timedelta
import pytz

# Define the currency pair and timeframe
symbol = "CHFJPY=X"  # CHF/JPY currency pair
interval = "1m"  # 5-minute historical data

# Define the time zone (e.g., UTC)
timezone = pytz.timezone("Europe/London")

# Get the current UTC time
end_date = datetime.now(timezone)

# Calculate the start date by subtracting 5 minutes from the current UTC time
start_date = end_date - timedelta(minutes=10)

# Convert the start and end dates to UTC time zone
start_date = start_date.astimezone(timezone)
end_date = end_date.astimezone(timezone)

# Fetch historical data from Yahoo Finance using UTC time
data = yf.download(symbol, start=start_date, end=end_date, interval=interval)

# Extract closing prices from the historical data
prices = data["Close"].values

# Calculate the indicators based on historical data
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
print("Buy Signal:", buy_signal[-1])
print("Sell Signal:", sell_signal[-1])

