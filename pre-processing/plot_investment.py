import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files into DataFrames
monthly_investment_df = pd.read_csv('monthly_investment_schedule.csv', parse_dates=['Date'])
daily_investment_df = pd.read_csv('daily_investment_schedule.csv', parse_dates=['Date'])

# Ensure 'Date' is in datetime format and sort the data
monthly_investment_df['Date'] = pd.to_datetime(monthly_investment_df['Date'])
daily_investment_df['Date'] = pd.to_datetime(daily_investment_df['Date'])

# Calculate cumulative investments
monthly_investment_df = monthly_investment_df.sort_values('Date').reset_index(drop=True)
daily_investment_df = daily_investment_df.sort_values('Date').reset_index(drop=True)

monthly_investment_df['Cumulative Investment'] = monthly_investment_df['Investment'].cumsum()
daily_investment_df['Cumulative Investment'] = daily_investment_df['Investment'].cumsum()

# Create a time range that covers the entire period of both investment schedules
all_dates = pd.date_range(start=min(monthly_investment_df['Date'].min(), daily_investment_df['Date'].min()), 
                          end=max(monthly_investment_df['Date'].max(), daily_investment_df['Date'].max()))

# Reindex both DataFrames to this new time range to align the dates
monthly_investment_df = monthly_investment_df.set_index('Date').reindex(all_dates).fillna(0).reset_index()
daily_investment_df = daily_investment_df.set_index('Date').reindex(all_dates).fillna(0).reset_index()

# Fill cumulative investments
monthly_investment_df['Cumulative Investment'] = monthly_investment_df['Investment'].cumsum()
daily_investment_df['Cumulative Investment'] = daily_investment_df['Investment'].cumsum()

# Plot the cumulative investments
plt.figure(figsize=(12, 6))
plt.plot(monthly_investment_df['index'], monthly_investment_df['Cumulative Investment'], label='Monthly Investment')
plt.plot(daily_investment_df['index'], daily_investment_df['Cumulative Investment'], label='Daily Investment', linestyle='--')

plt.xlabel('Date')
plt.ylabel('Cumulative Investment')
plt.title('Cumulative Investment Comparison')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save or show the plot
plt.savefig('cumulative_investment_comparison.png')
plt.show()