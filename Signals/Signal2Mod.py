import talib
import yfinance as yf
from datetime import datetime

# Define the currency pair and timeframe
symbol = "NZDCHF=X"  # CHF/JPY currency pair
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
#buy_signal = (sma_short > sma_long) & (rsi < 30) & (prices < lower_band)
#sell_signal = (sma_short < sma_long) & (rsi > 70) & (prices > upper_band)

# Print the signals
#current_index = len(prices) - 1
#print("Buy Signal:", buy_signal[current_index])
#print("Sell Signal:", sell_signal[current_index])
buy_signal = 0
sell_signal = 0
sma_buy = 0
sma_sell = 0
rsi_buy = 0
rsi_sell = 0
bollinger_buy = 0
bollinger_sell = 0

for i in range(len(data)):
    if sma_short[i] > sma_short[i]:
        sma_buy = sma_buy+1
    elif sma_short[i] < sma_short[i]:
        sma_sell = sma_sell+1
    if rsi[i] < 30 :
        rsi_buy = rsi_buy+1
    elif rsi[i] > 70:
        rsi_sell = rsi_sell+1
    if prices[i] < lower_band[i] :
        bollinger_buy = bollinger_buy+1
    elif prices[i] > upper_band[i]:
        bollinger_sell = bollinger_sell+1

if sma_buy > sma_sell:
    buy_signal = buy_signal+1
if rsi_buy > rsi_sell:
    buy_signal = buy_signal+1
if bollinger_buy > bollinger_sell:
    buy_signal = buy_signal+1
if sma_buy < sma_sell:
    sell_signal = sell_signal+1
if rsi_buy < rsi_sell:
    sell_signal = sell_signal+1
if bollinger_buy < bollinger_sell:
    sell_signal = sell_signal+1

if sell_signal>buy_signal:
    print('Sell')
elif buy_signal>sell_signal:
    print('Buy')
else:
    print('UR BRAIN')