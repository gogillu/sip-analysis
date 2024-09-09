import pandas as pd
import os

# Define the directories
daily_investment_file = 'fine_tuned_daily_investment_with_all_dates_with_returns.csv'
monthly_investment_dir = 'fine_tuned_monthly_investment_schedules_with_units_all_dates_with_returns'
output_file = 'final_investment_summary.csv'

# Initialize a list to store the results
investment_summary = []

# Process the daily investment file
df_daily = pd.read_csv(daily_investment_file)
last_row_daily = df_daily.iloc[-1]  # Get the last row
investment_summary.append({
    'File': 'Daily Investment',
    'Total Invested': last_row_daily['Total Invested'],
    'Acquired Value': last_row_daily['Acquired Value']
})

# Process each monthly investment file
for filename in os.listdir(monthly_investment_dir):
    if filename.endswith('.csv'):
        # Load the monthly investment data
        df_monthly = pd.read_csv(os.path.join(monthly_investment_dir, filename))
        last_row_monthly = df_monthly.iloc[-1]  # Get the last row
        investment_summary.append({
            'File': filename[:-4],  # Use the filename without the .csv extension
            'Total Invested': last_row_monthly['Total Invested'],
            'Acquired Value': last_row_monthly['Acquired Value']
        })

# Convert the results to a DataFrame
summary_df = pd.DataFrame(investment_summary)

# Save the summary to a CSV file
summary_df.to_csv(output_file, index=False)

print(f"Investment summary has been saved to {output_file}.")