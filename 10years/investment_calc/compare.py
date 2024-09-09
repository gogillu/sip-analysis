import pandas as pd
import os
import matplotlib.pyplot as plt

# Define the directories
daily_investment_file = 'fine_tuned_daily_investment_with_all_dates_with_returns.csv'
monthly_investment_dir = 'fine_tuned_monthly_investment_schedules_with_units_all_dates_with_returns'
output_dir = 'investment_comparison_graphs'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load the daily investment data
df_daily = pd.read_csv(daily_investment_file)
df_daily['Date'] = pd.to_datetime(df_daily['Date'])

# Process each monthly investment file
for filename in os.listdir(monthly_investment_dir):
    if filename.endswith('.csv'):
        # Load the monthly investment data
        df_monthly = pd.read_csv(os.path.join(monthly_investment_dir, filename))
        df_monthly['Date'] = pd.to_datetime(df_monthly['Date'])

        # Plot the comparison graph
        plt.figure(figsize=(14, 8))
        plt.plot(df_daily['Date'], df_daily['Total Invested'], label='Total Invested (Daily)', color='blue')
        plt.plot(df_daily['Date'], df_daily['Acquired Value'], label='Acquired Value (Daily)', color='green')
        plt.plot(df_monthly['Date'], df_monthly['Total Invested'], label='Total Invested (Monthly)', color='orange')
        plt.plot(df_monthly['Date'], df_monthly['Acquired Value'], label='Acquired Value (Monthly)', color='red')

        # Customize the plot
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title(f'Investment Comparison: Daily vs Monthly ({filename})')
        plt.legend()
        plt.grid(True)

        # Save the graph to the output directory
        output_filepath = os.path.join(output_dir, f'comparison_{filename[:-4]}.png')
        plt.savefig(output_filepath)
        plt.close()

        print(f"Generated and saved: {output_filepath}")

print("All comparison graphs have been generated and saved in the output directory.")