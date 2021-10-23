import pandas as pd
import yfinance as yf
import time 

imported_names = pd.read_excel('name.xlsx')
stock_symbols = imported_names['Symbol'].tolist()
ticker_object = yf.Ticker('AAPL')
df_columns = ticker_object.info.keys()
df = pd.DataFrame(columns=df_columns)

for name in stock_symbols:
	ticker_object = yf.Ticker(name)
	time.sleep(0.5)
	df = df.append(ticker_object.info,ignore_index=True)
	i = i +1 

df.to_excel('data.xlsx')
