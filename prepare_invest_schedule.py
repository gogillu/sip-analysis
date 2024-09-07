import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

# Load Sensex index data
def load_data(filename):
    return pd.read_csv(filename, parse_dates=['Date'], index_col='Date')

# Schedule 1: Investing ₹30,000 on the 1st of every month
def generate_monthly_investment_schedule(start_date, end_date, amount):
    dates = pd.date_range(start=start_date, end=end_date, freq='MS')
    investment_schedule = pd.DataFrame(index=dates)
    investment_schedule['Investment'] = amount
    investment_schedule.index.name = 'Date'
    return investment_schedule

# Schedule 2: Investing ₹30,000 evenly across market open days each month
def generate_daily_investment_schedule(data, amount):
    investment_schedule = pd.DataFrame()
    
    # Iterate over months in the data
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

# Define start and end dates
start_date = '2015-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')
amount = 30000

# Generate schedules
monthly_investment_schedule = generate_monthly_investment_schedule(start_date, end_date, amount)

# Load Sensex data
sensex_data = load_data('sensex_index_data.csv')

# Generate daily investment schedule
daily_investment_schedule = generate_daily_investment_schedule(sensex_data, amount)

# Save CSV files
monthly_investment_schedule.to_csv('monthly_investment_schedule.csv')
daily_investment_schedule.to_csv('daily_investment_schedule.csv')

# Combine and plot
combined = pd.DataFrame({
    'Monthly Investment': monthly_investment_schedule['Investment'],
    'Daily Investment': daily_investment_schedule.groupby(daily_investment_schedule.index.to_period('M')).sum()['Investment']
})

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(combined.index, combined['Monthly Investment'], label='Monthly Investment', marker='o')
plt.plot(combined.index, combined['Daily Investment'], label='Daily Investment', marker='x')
plt.xlabel('Date')
plt.ylabel('Amount Invested')
plt.title('Investment Schedule Comparison')
plt.legend()
plt.grid(True)

# Save the plot
output_folder = 'investment_schedules'
os.makedirs(output_folder, exist_ok=True)
plt.savefig(f'{output_folder}/investment_schedule_comparison.png')

print("Schedules and graph generated successfully.")