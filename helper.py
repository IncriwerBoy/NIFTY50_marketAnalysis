import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns



stock_symbols = [
    'ADANIENT.NS', 'APOLLOHOSP.NS', 'ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS',
    'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS', 'BPCL.NS',
    'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS',
    'EICHERMOT.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'GRASIM.NS', 'HINDUNILVR.NS',
    'ICICIBANK.NS', 'INFY.NS', 'ITC.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS',
    'LT.NS', 'MARUTI.NS', 'M&M.NS', 'NESTLEIND.NS', 'NTPC.NS',
    'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'HCLTECH.NS',
    'SHREECEM.NS', 'SUNPHARMA.NS', 'TATASTEEL.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS',
    'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'WIPRO.NS', 'HEROMOTOCO.NS',
    'HINDALCO.NS', 'INDUSINDBK.NS', 'LTIM.NS', 'BAJFINANCE.NS', 'TCS.NS'
]


def raw_data():
    stock_data = pd.read_csv('indian_stocks_data.csv')
    financial_data = pd.read_csv('financial_data.csv')
    gdp = pd.read_csv('gdp_cpi.csv')
    inflation_rate = pd.read_csv('inflation_rate.csv')

    
    #-----------------------------Data Cleaning-----------------------------    
    gdp['date'] = pd.to_datetime(gdp['date'])
    inflation_rate['date'] = pd.to_datetime(inflation_rate['date'])
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data.rename(columns={'Date': 'date'}, inplace=True)
    
    gdp = gdp[gdp['date'] >= '2015-01-01']
    inflation_rate = inflation_rate[inflation_rate['date'] >= '2015-01-01']
    
    return stock_data, financial_data, inflation_rate, gdp


# Data Collection
def data_collect():
    
    stock_data = pd.read_csv('indian_stocks_data.csv')
    financial_data = pd.read_csv('financial_data.csv')
    gdp = pd.read_csv('gdp_cpi.csv')
    inflation_rate = pd.read_csv('inflation_rate.csv')

    
    #-----------------------------Data Cleaning-----------------------------    
    gdp['date'] = pd.to_datetime(gdp['date'])
    inflation_rate['date'] = pd.to_datetime(inflation_rate['date'])
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data.rename(columns={'Date': 'date'}, inplace=True)
    
    gdp = gdp[gdp['date'] >= '2015-01-01']
    inflation_rate = inflation_rate[inflation_rate['date'] >= '2015-01-01']
    
    # Join historical stock prices with the financial ratios dataframe
    combined_df = stock_data.reset_index().merge(financial_data, on='Stock', how='left')
    combined_df2 = gdp.merge(inflation_rate, on='date', how='left')
    
    #---------------------------Feature Engineering------------------------
    
    # Create new features
    # Example: Calculate moving average
    combined_df['MA_50'] = combined_df['Close'].rolling(window=50).mean()
    for i in range(0, 50):
        combined_df['MA_50'].iloc[i] = combined_df['Close'].iloc[i]
    
    # Calculate daily returns
    combined_df['Daily_Return'] = combined_df['Adj Close'].pct_change()
    combined_df['Rolling_Volatility'] = combined_df['Daily_Return'].rolling(window=30).std() * (252 ** 0.5)
    for i in range(0, 30):
        combined_df['Rolling_Volatility'].iloc[i] = combined_df['Daily_Return'].iloc[i] * (252 ** 0.5)
    combined_df.set_index('index', inplace=True)
    
    
    #--------------------------Merging both the data------------------------
    features1 = list(combined_df.columns)
    features1.remove('date')
    features1.remove('Stock')

    features2 = list(combined_df2.columns)
    features2.remove('date')

    merged_df = combined_df.merge(combined_df2, on='date', how='left')
    merged_df[features2] = merged_df[features2].fillna(method = 'bfill')
    merged_df[features2] = merged_df[features2].fillna(method = 'ffill')

    merged_df.drop(columns = ' ', inplace=True)
    merged_df['PE_Ratio'] = merged_df['PE_Ratio'].fillna(method = 'bfill')
    merged_df.dropna(inplace=True)
    
    return merged_df, combined_df, combined_df2

