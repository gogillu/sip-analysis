import pandas as pd
import os

# Define the input and output directories
input_dir = 'fine_tuned_monthly_investment_schedules_with_units_all_dates'
output_dir = 'fine_tuned_monthly_investment_schedules_with_units_all_dates_with_returns'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        # Load the CSV file into a DataFrame
        df = pd.read_csv(os.path.join(input_dir, filename))

        # Calculate the cumulative units purchased
        df['Cumulative Units Purchased'] = df['Units Purchased'].cumsum()

        # Calculate the total invested amount
        df['Total Invested'] = df['Investment'].cumsum()

        # Calculate the acquired value
        df['Acquired Value'] = df['Cumulative Units Purchased'] * df['Adj Close']

        # Save the updated DataFrame to a new CSV file in the output directory
        output_filepath = os.path.join(output_dir, filename)
        df.to_csv(output_filepath, index=False)

        print(f"Processed and saved: {filename}")

print("All files have been processed and saved in the output directory.")