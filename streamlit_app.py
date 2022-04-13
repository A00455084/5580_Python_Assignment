import streamlit as st
import pandas as pd
import requests
import numpy as np

st.title('Bitcoin Prices')

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

payload={'vs_currency':'cad','days':90,'interval':'daily'}
headers = {}

response = requests.request("GET", url, headers=headers, params=payload)
if response.status_code==200:
    data = response.json()


data_df = pd.DataFrame(data=data['prices'],columns=['Date','Price'])
print(data_df.head())
data_df['Date'] = pd.to_datetime(data_df['Date'],unit='ms',origin='unix')
data_df.set_index('Date',inplace=True)
st.line_chart(data_df)