import pandas as pd
import yfinance as yf

# Define the ticker symbol for the Sensex index
ticker_symbol = '^BSESN'  # BSE Sensex index ticker

# Download historical data
def download_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Define the time period for the past 10 years
end_date = pd.Timestamp.now().strftime('%Y-%m-%d')
start_date = (pd.Timestamp.now() - pd.DateOffset(years=10)).strftime('%Y-%m-%d')

# Get the data
data = download_data(ticker_symbol, start_date, end_date)

# Save the data to a CSV file
data.to_csv('sensex_index_data.csv')

print("Data downloaded and saved to 'sensex_index_data.csv'")