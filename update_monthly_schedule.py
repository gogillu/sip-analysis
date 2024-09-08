import pandas as pd

# Load the Sensex index data into a DataFrame
sensex_df = pd.read_csv('sensex_index_data.csv', parse_dates=['Date'])

# Load the monthly investment schedule into a DataFrame
monthly_investment_df = pd.read_csv('monthly_investment_schedule.csv', parse_dates=['Date'])

# Ensure 'Date' is in datetime format and sort the data
sensex_df['Date'] = pd.to_datetime(sensex_df['Date'])
monthly_investment_df['Date'] = pd.to_datetime(monthly_investment_df['Date'])

# Get a set of dates when the market was open
open_market_dates = set(sensex_df['Date'])

# Initialize a list to store the updated investment dates
updated_investment_dates = []

# Iterate over the monthly investment dates
for index, row in monthly_investment_df.iterrows():
    original_date = row['Date']
    investment_amount = row['Investment']

    # Check if the original investment date is in the open market dates
    if original_date in open_market_dates:
        updated_investment_dates.append((original_date, investment_amount))
    else:
        # If the market was closed on the original date, find the next available open date
        next_open_date = sensex_df[sensex_df['Date'] > original_date]['Date'].min()
        updated_investment_dates.append((next_open_date, investment_amount))

# Create a new DataFrame with the updated investment dates
updated_investment_df = pd.DataFrame(updated_investment_dates, columns=['Date', 'Investment'])

# Save the updated investment schedule to a new CSV file
updated_investment_df.to_csv('updated_monthly_investment_schedule.csv', index=False)

print("Updated investment schedule saved to 'updated_monthly_investment_schedule.csv'")