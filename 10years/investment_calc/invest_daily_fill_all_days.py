import pandas as pd
from datetime import datetime, timedelta

# Load the CSV file into a DataFrame
df = pd.read_csv('fine_tuned_daily_investment_with_units.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Generate a complete date range from the minimum to the maximum date in the DataFrame
full_date_range = pd.date_range(start=df['Date'].min(), end=df['Date'].max())

# Reindex the DataFrame to include all dates from the full_date_range
df_full = df.set_index('Date').reindex(full_date_range).reset_index()

# Rename the index column back to 'Date'
df_full = df_full.rename(columns={'index': 'Date'})

# Fill missing values in the 'Investment' and 'Units Purchased' columns with 0
df_full['Investment'].fillna(0, inplace=True)
df_full['Units Purchased'].fillna(0, inplace=True)

# Forward fill the 'Adj Close' column to fill in missing values
df_full['Adj Close'].fillna(method='bfill', inplace=True)

# Save the updated DataFrame to a new CSV file
df_full.to_csv('fine_tuned_daily_investment_with_all_dates.csv', index=False)

print("Updated CSV file has been saved as 'fine_tuned_daily_investment_with_all_dates.csv'")