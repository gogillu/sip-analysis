import os
import pandas as pd

# Load the Sensex index data into a DataFrame
sensex_df = pd.read_csv('../sensex_index_data.csv', parse_dates=['Date'])

# Ensure 'Date' is in datetime format and sort the data
sensex_df['Date'] = pd.to_datetime(sensex_df['Date'])
sensex_df = sensex_df.sort_values(by='Date')

# Get a set of dates when the market was open
open_market_dates = set(sensex_df['Date'])

# Create output directory if it doesn't exist
output_dir = 'fine_tuned_monthly_investment_schedules'
os.makedirs(output_dir, exist_ok=True)

# Iterate over all CSV files in the monthly_investment_schedules folder
input_dir = 'monthly_investment_schedules'
for file_name in os.listdir(input_dir):
    if file_name.endswith('.csv'):
        # Load the monthly investment schedule into a DataFrame
        file_path = os.path.join(input_dir, file_name)
        monthly_investment_df = pd.read_csv(file_path, parse_dates=['Date'])
        
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

        # Save the updated investment schedule to a new CSV file in the output directory
        output_file_path = os.path.join(output_dir, file_name)
        updated_investment_df.to_csv(output_file_path, index=False)

        print(f"Updated investment schedule saved to '{output_file_path}'")