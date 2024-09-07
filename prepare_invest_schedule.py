import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data and generate schedules as before
def load_data(filename):
    return pd.read_csv(filename, parse_dates=['Date'], index_col='Date')

# Define start and end dates
start_date = '2015-01-01'
end_date = pd.Timestamp.now().strftime('%Y-%m-%d')
amount = 30000

# Generate monthly investment schedule
def generate_monthly_investment_schedule(start_date, end_date, amount):
    dates = pd.date_range(start=start_date, end=end_date, freq='MS')
    investment_schedule = pd.DataFrame(index=dates)
    investment_schedule['Investment'] = amount
    investment_schedule.index.name = 'Date'
    return investment_schedule

# Generate daily investment schedule
def generate_daily_investment_schedule(data, amount):
    investment_schedule = pd.DataFrame()
    
    for month_start in pd.date_range(start=data.index.min(), end=data.index.max(), freq='MS'):
        month_end = month_start + pd.DateOffset(months=1) - pd.DateOffset(days=1)
        market_days = data.loc[month_start:month_end].index.to_list()
        
        if market_days:
            daily_investment = amount / len(market_days)
            temp_df = pd.DataFrame(index=market_days)
            temp_df['Investment'] = daily_investment
            investment_schedule = pd.concat([investment_schedule, temp_df])
    
    investment_schedule.index.name = 'Date'
    return investment_schedule

# Generate schedules
monthly_investment_schedule = generate_monthly_investment_schedule(start_date, end_date, amount)
sensex_data = load_data('sensex_index_data.csv')
daily_investment_schedule = generate_daily_investment_schedule(sensex_data, amount)

# Calculate cumulative investments
monthly_investment_schedule['Cumulative'] = monthly_investment_schedule['Investment'].cumsum()
daily_investment_schedule['Cumulative'] = daily_investment_schedule['Investment'].cumsum()

# Resample daily data to monthly for comparison
daily_investment_monthly = daily_investment_schedule.resample('M').sum()
combined_cumulative = pd.DataFrame({
    'Monthly Cumulative': monthly_investment_schedule['Cumulative'],
    'Daily Cumulative': daily_investment_monthly['Cumulative']
})

# Print the values for debugging
print("Monthly Cumulative Investment:")
print(monthly_investment_schedule[['Cumulative']].head())
print(monthly_investment_schedule[['Cumulative']].tail())

print("\nDaily Cumulative Investment:")
print(daily_investment_schedule[['Cumulative']].head())
print(daily_investment_schedule[['Cumulative']].tail())

print("\nCombined Cumulative Investment:")
print(combined_cumulative.head())
print(combined_cumulative.tail())

# Plot cumulative data
plt.figure(figsize=(12, 6))
plt.plot(combined_cumulative.index, combined_cumulative['Monthly Cumulative'], label='Monthly Cumulative Investment', marker='o')
plt.plot(combined_cumulative.index, combined_cumulative['Daily Cumulative'], label='Daily Cumulative Investment', marker='x')
plt.xlabel('Date')
plt.ylabel('Cumulative Investment')
plt.title('Cumulative Investment Comparison')
plt.legend()
plt.grid(True)

# Save the plot
output_folder = 'investment_schedules'
os.makedirs(output_folder, exist_ok=True)
plt.savefig(f'{output_folder}/cumulative_investment_comparison.png')

print("Cumulative investment plot generated and saved successfully.")