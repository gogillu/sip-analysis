import pandas as pd

# Load the Sensex index data
sensex_df = pd.read_csv('sensex_index_data.csv', parse_dates=['Date'])

# Load the daily investment schedule
daily_investment_df = pd.read_csv('fine_tuned_daily_investment_schedule.csv', parse_dates=['Date'])

# Merge the investment schedule with the Sensex data to get the Adj Close price for each investment date
merged_df = pd.merge(daily_investment_df, sensex_df[['Date', 'Adj Close']], on='Date', how='left')

# Calculate the number of units purchased on each investment date
merged_df['Units Purchased'] = merged_df['Investment'] / merged_df['Adj Close']

# Save the result to a new CSV file
output_file = 'fine_tuned_daily_investment_with_units.csv'
merged_df.to_csv(output_file, index=False)

print(f"Output saved to {output_file}")