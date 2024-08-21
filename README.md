# Nifty 50 Market Analysis

## Overview

This project provides an analysis of the Nifty 50 stock market data and related financial indicators over the past 9 years. It includes data on stock prices, financial metrics (like P/E ratios and market cap), inflation rates, and GDP. The project involves data collection, cleaning, preprocessing, feature engineering, exploratory data analysis (EDA), and visualization. The final analysis is deployed using Streamlit and can be accessed via the following link: [Project Dashboard](https://nifty50marketanalysis.streamlit.app).

## Data Files

The project utilizes the following CSV files:

1. **inflation_rate.csv**: Contains historical inflation rate data for India over the past years.
2. **gdp.csv**: Provides GDP data for India over the past years.
3. **indian_stock_data.csv**: Includes stock market data for Nifty 50 companies, including prices and other relevant metrics.
4. **financial_data.csv**: Contains financial metrics for the Nifty 50 stocks, such as P/E ratios and market capitalization.

## Project Workflow

### 1. Data Collection

- **Sources**: Data was collected from reliable financial sources and APIs.
- **Files**: The collected data is saved in the four CSV files mentioned above.

### 2. Data Cleaning and Preprocessing

- **Data Cleaning**: Removed duplicates, handled missing values, and corrected any inconsistencies.
- **Feature Engineering**: Added new features such as rolling volatility and monthly/annual averages.
- **Preprocessing**: Normalized and scaled features, encoded categorical variables, and merged datasets.

### 3. Exploratory Data Analysis (EDA)

- **Correlation Heatmaps**: Visualized correlations between various financial metrics.
- **Pairplots**: Analyzed relationships between stock prices and financial metrics.
- **Time Series Analysis**: Studied trends in stock prices, inflation rates, and GDP over time.
- **Histograms and Bar Charts**: Examined the distribution of financial metrics like P/E ratios.

### 4. Deployment

- **Platform**: Deployed the project using Streamlit, providing an interactive web-based dashboard.
- **Link**: [Project Dashboard](https://nifty50marketanalysis.streamlit.app)

## Visualizations

The Streamlit application includes the following visualizations:

1. **Inflation Rate Over Time**: Shows how inflation rates have varied year by year.
2. **GDP Over Time**: Displays the trend of GDP in India.
3. **Stock Prices Over Time**: Tracks the historical stock prices of Nifty 50 companies.
4. **Stock Price and Volatility**: Plots stock prices and their volatility over time.
5. **PE Ratio by Stock**: Shows the P/E ratios for the top 10 stocks with the highest ratios.
6. **Market Capitalization Over Time**: Displays the trend in market capitalization for the stocks.
7. **Distribution of P/E Ratio**: Analyzes the distribution of P/E ratios across stocks.
8. **Inflation Rate and GDP Over Time**: Provides a combined view of inflation rate and GDP trends.
9. **Correlation Heatmap of Key Metrics**: Visualizes correlations between stock prices, GDP, and inflation rates.
10. **Average Monthly and Yearly Close Prices**: Shows the average close prices on a monthly and yearly basis.

## Setup

To run this project locally:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Dependencies

- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`
- `numpy`
- `yfinance`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
