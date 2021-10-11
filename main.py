import pandas as pd
import yfinance as yf
import streamlit as st

nasdaq_tickers = pd.read_excel('name.xlsx')  
tickers_list = nasdaq_tickers['Symbol']
tickers_data = {}

st.header('MarketData')

data_of_interest = ['symbol','longName','website','targetMeanPrice','recommendationMean','regularMarketDayLow','regularMarketDayHigh']
df = pd.DataFrame(columns=data_of_interest)
selected_ticker = st.multiselect('Select tickers', tickers_list)

st.text('Select ticker(s) or upload a csv with ticker(s) inside')

data_file = st.file_uploader("Upload CSV",type=['csv'])

if data_file is not None:
    nasdaq_tickers = pd.read_csv(data_file)
    st.dataframe(nasdaq_tickers['Symbol'])
    selected_ticker = nasdaq_tickers['Symbol'].tolist()

def get_data_of_interest(data):
    value_of_interest = {}
    for name_of_interest in data_of_interest:
        value_of_interest[name_of_interest] = data.get(name_of_interest)        
    return value_of_interest

@st.cache
def convert_df(df):
# IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

if st.button('Get Data') and selected_ticker:
    for ticker in selected_ticker:
        ticker_object = yf.Ticker(ticker)
        values_of_interest = get_data_of_interest(ticker_object.info)
        df = df.append(values_of_interest,ignore_index=True)
    st.dataframe(df)
    csv = convert_df(df)
    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
    )