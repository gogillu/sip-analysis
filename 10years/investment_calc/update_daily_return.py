import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('fine_tuned_daily_investment_with_all_dates.csv')

# Calculate the cumulative units purchased
df['Cumulative Units Purchased'] = df['Units Purchased'].cumsum()

# Calculate the total invested amount
df['Total Invested'] = df['Investment'].cumsum()

# Calculate the acquired value
df['Acquired Value'] = df['Cumulative Units Purchased'] * df['Adj Close']

# Save the updated DataFrame to a new CSV file
df.to_csv('fine_tuned_daily_investment_with_all_dates_with_returns.csv', index=False)

print("Updated CSV file has been saved as 'fine_tuned_daily_investment_with_all_dates_with_returns.csv'")