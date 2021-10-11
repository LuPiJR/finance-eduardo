import pandas as pd
import yfinance as yf
from bs4 import BeautifulSoup
from pandas_datareader import data as pdr

tickers_list = ['AAPL']
tickers_data = {}
apple = yf.Ticker("AAPL")
#apple = yf.Ticker("AAPL")

#yf.pdr_override() # <== that's all it takes :-)

# download dataframe
#data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
#print(data)


for ticker in tickers_list:
    ticker_object = yf.Ticker(ticker)
    temp = pd.DataFrame.from_dict(ticker_object.info, orient='index')
    temp.reset_index(inplace=True)
    temp.columns = ['Attribute','Recent']
    tickers_data[ticker] = temp

combined_data = pd.concat(tickers_data)
combined_data = combined_data.reset_index()

del combined_data['level_1']
combined_data.columns = ['Ticker','Attribute','Recent']

print(combined_data)
print(apple.financials)

#combined_data.to_excel('combined_data.xlsx')
#recommendationMean

