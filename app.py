import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import helper

# Page Title
st.title("Nifty 50 Market Analysis")

# Data Collection
merged_df, market_df, economic_df = helper.data_collect()

# Section 1: Key Economic Indicators
st.header("Key Economic Indicators")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Highest Inflated Year")
    highest_inflation_year = economic_df.sort_values(by=' Inflation Rate (%)', ascending=False).head(1)['date'].dt.year.values[0]
    st.metric(label="Year", value=highest_inflation_year)
    st.write(f"The year {highest_inflation_year} experienced the highest inflation rate during the period, which indicates a significant rise in prices and potential economic challenges.")

with col2:
    st.subheader("Highest GDP Year")
    highest_gdp_year = economic_df.sort_values(by=[' GDP ( Billions of US $)', ' Per Capita (US $)'], ascending=False).head(1)['date'].dt.year.values[0]
    st.metric(label="Year", value=highest_gdp_year)
    st.write(f"The year {highest_gdp_year} saw the highest GDP, reflecting strong economic growth and higher production of goods and services in the country.")

# Section 2: Economic Trends
st.header("Economic Trends")

# Inflation Trend
st.subheader("Inflation Rate Over Time")
st.line_chart(economic_df.set_index('date')[' Inflation Rate (%)'])
st.write("This chart shows the trend of inflation over the years. An increasing trend indicates rising prices, while a decreasing trend suggests deflation or stable prices. Understanding this trend is crucial for assessing the purchasing power and cost of living over time.")

# GDP Trend
st.subheader("GDP Over Time")
st.line_chart(economic_df.set_index('date')[' GDP ( Billions of US $)'])
st.write("The GDP trend provides insight into the overall economic performance of the country. An upward trend in GDP typically indicates economic growth, while a downward trend may signal economic downturns or recessions.")

# Section 3: Correlations
st.header("Correlation Analysis")

# Correlation Heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(merged_df.drop(columns=['date', 'Stock']).corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)
st.write("The heatmap shows the correlation between various financial and economic indicators. High positive correlation values (close to 1) suggest a strong relationship between the variables, whereas negative values indicate an inverse relationship. This analysis helps in understanding how different factors like stock prices, PE ratios, and market capitalization are interrelated.")

# Pairplot of Selected Features
st.header("Pairplot of Selected Features")
fig = sns.pairplot(merged_df[['Close', 'PE_Ratio', 'Dividend_Yield', 'Market_Cap']])
st.pyplot(fig.fig)
st.write("The pairplot visualizes the relationships between selected financial features. It allows for the examination of possible linear or non-linear relationships between variables like Close prices, PE ratios, Dividend yields, and Market capitalization, helping to identify trends or anomalies.")

# Section 4: Market Analysis
st.header("Market Analysis")

# Stock Prices Over Time
st.subheader("Stock Prices Over Time")
fig, ax = plt.subplots()
market_df.set_index('date')['Close'].plot(title='Stock Prices Over Time', ax=ax)
ax.set_xlabel('Date')
ax.set_ylabel('Close Price')
st.pyplot(fig)
st.write("This chart illustrates the fluctuations in stock prices over time. Tracking these changes is essential for investors to identify potential buy or sell opportunities and to understand market volatility.")

# Stock Price and Volatility Over Time
st.subheader("Stock Price and Volatility Over Time")
fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
market_df.set_index('date')['Close'].plot(ax=ax[0], title='Stock Price Over Time')
market_df.set_index('date')['Rolling_Volatility'].plot(ax=ax[1], title='Rolling Volatility Over Time')
plt.tight_layout()
st.pyplot(fig)
st.write("This dual chart compares stock prices with their corresponding volatility over time. While the upper chart shows price movements, the lower chart reflects the volatility, providing insight into the stability of stock prices. Higher volatility often indicates higher risk.")

# PE Ratio by Stock
st.subheader("PE Ratio by Stock")
temp_df = market_df[['Stock', 'PE_Ratio']].drop_duplicates().sort_values(by='PE_Ratio', ascending=False).head(10)
fig, ax = plt.subplots()
sns.barplot(data=temp_df, x='Stock', y='PE_Ratio', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_xlabel('Stock')
ax.set_ylabel('PE Ratio')
ax.set_title('Top 10 Stocks by PE Ratio')
st.pyplot(fig)
st.write("This bar chart displays the top 10 stocks based on their PE ratios. A higher PE ratio can indicate that a stock is overvalued, while a lower PE ratio might suggest it is undervalued. Investors often use this metric to assess the relative value of stocks.")

# Market Capitalization Over Time
st.subheader("Market Capitalization Over Time")
fig, ax = plt.subplots()
market_df['Market_Cap'].plot(title='Market Capitalization Over Time', ax=ax)
st.pyplot(fig)
st.write("The market capitalization trend shows how the total value of the market has changed over time. It's an essential metric for understanding the scale and size of companies within the Nifty 50 and their collective impact on the market.")

# Section 5: Distributions and Correlations
st.header("Distributions and Correlations")

# Distribution of P/E Ratio
st.subheader("Distribution of P/E Ratio")
fig, ax = plt.subplots()
sns.histplot(market_df['PE_Ratio'], kde=True, bins=30, ax=ax)
ax.set_xlabel('PE Ratio')
ax.set_title('Distribution of P/E Ratio')
st.pyplot(fig)
st.write("This histogram displays the distribution of PE ratios across stocks, helping to identify the most common ranges and any outliers. The presence of a KDE (Kernel Density Estimate) line allows for a smoother interpretation of the distribution.")

# Inflation Rate and GDP Over Time
st.subheader("Inflation Rate and GDP Over Time")
fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
sns.lineplot(data=economic_df, x='date', y=' Inflation Rate (%)', ax=axs[0], color='blue')
axs[0].set_title('Inflation Rate Over Time')
axs[0].set_ylabel('Inflation Rate (%)')
sns.lineplot(data=economic_df, x='date', y=' GDP ( Billions of US $)', ax=axs[1], color='green')
axs[1].set_title('GDP Over Time')
axs[1].set_ylabel('GDP (Billions of US $)')
axs[1].set_xlabel('Date')
plt.tight_layout()
st.pyplot(fig)
st.write("These two charts show how inflation and GDP have evolved over time. Analyzing these trends together can provide insights into the economic environment, as inflation and GDP are often inversely related, with high inflation potentially hindering GDP growth.")

# Correlation Heatmap of Close Price, GDP, and Inflation Rate
st.subheader("Correlation Heatmap: Close Price, GDP, and Inflation Rate")
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(merged_df[['Close', ' GDP ( Billions of US $)', ' Inflation Rate (%)']].corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)
st.write("This heatmap focuses on the correlation between stock prices, GDP, and inflation rate. The relationships between these variables are crucial for understanding how macroeconomic factors influence stock market performance.")

# Section 6: Monthly and Yearly Averages
st.header("Monthly and Yearly Averages")

# Average Monthly Close Prices
st.subheader("Average Monthly Close Prices")
merged_df['Month'] = pd.to_datetime(merged_df['date']).dt.month
monthly_avg = merged_df.groupby('Month')['Close'].mean()
fig, ax = plt.subplots()
monthly_avg.plot(kind='line', title='Average Monthly Close Prices', ax=ax)
st.pyplot(fig)
st.write("This line chart shows the average monthly closing prices. Observing the monthly averages can reveal seasonal trends in stock prices, helping investors plan their trades accordingly.")

# Average Yearly Close Prices
st.subheader("Average Yearly Close Prices")
merged_df['Year'] = pd.to_datetime(merged_df['date']).dt.year
yearly_avg = merged_df.groupby('Year')['Close'].mean()
fig, ax = plt.subplots()
yearly_avg.plot(kind='line', title='Average Yearly Close Prices', ax=ax)
st.pyplot(fig)
st.write("This chart shows the average yearly closing prices. It helps in identifying long-term trends and overall market performance year over year, providing a broader perspective on market movements.")
