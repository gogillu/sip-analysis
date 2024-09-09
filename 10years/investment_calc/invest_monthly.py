import pandas as pd
import os

# File paths
sensex_file = 'sensex_index_data.csv'
input_folder = 'fine_tuned_monthly_investment_schedules'
output_folder = 'fine_tuned_monthly_investment_schedules_with_units'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the Sensex index data
sensex_df = pd.read_csv(sensex_file, parse_dates=['Date'])

# Process each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        # Load the monthly investment schedule
        monthly_investment_df = pd.read_csv(os.path.join(input_folder, filename), parse_dates=['Date'])
        
        # Merge the investment schedule with the Sensex data to get the Adj Close price for each investment date
        merged_df = pd.merge(monthly_investment_df, sensex_df[['Date', 'Adj Close']], on='Date', how='left')
        
        # Calculate the number of units purchased on each investment date
        merged_df['Units Purchased'] = merged_df['Investment'] / merged_df['Adj Close']
        
        # Save the result to a new CSV file in the output folder
        output_file = os.path.join(output_folder, filename.replace('.csv', '_with_units.csv'))
        merged_df.to_csv(output_file, index=False)
        
        print(f"Processed and saved: {output_file}")

print("All files processed and saved.")