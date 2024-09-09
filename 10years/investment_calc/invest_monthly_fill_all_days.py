import pandas as pd
import os

# Define the input and output directories
input_dir = 'fine_tuned_monthly_investment_schedules_with_units'
output_dir = 'fine_tuned_monthly_investment_schedules_with_units_all_dates'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load the sensex index data into a DataFrame
sensex_data = pd.read_csv('sensex_index_data.csv')
sensex_data['Date'] = pd.to_datetime(sensex_data['Date'])
sensex_data.set_index('Date', inplace=True)

# Process each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        # Load the CSV file into a DataFrame
        df = pd.read_csv(os.path.join(input_dir, filename))

        # Convert the 'Date' column to datetime format
        df['Date'] = pd.to_datetime(df['Date'])

        # Generate a complete date range from the minimum to the maximum date in the DataFrame
        full_date_range = pd.date_range(start=df['Date'].min(), end=df['Date'].max())

        # Reindex the DataFrame to include all dates from the full_date_range
        df_full = df.set_index('Date').reindex(full_date_range).reset_index()

        # Rename the index column back to 'Date'
        df_full = df_full.rename(columns={'index': 'Date'})

        # Fill missing values in the 'Investment' and 'Units Purchased' columns with 0
        df_full['Investment'].fillna(0, inplace=True)
        df_full['Units Purchased'].fillna(0, inplace=True)

        # Merge with sensex data to fill missing 'Adj Close' values
        df_full = df_full.merge(sensex_data[['Adj Close']], on='Date', how='left', suffixes=('', '_sensex'))

        # Fill missing 'Adj Close' values using the sensex data
        df_full['Adj Close'] = df_full['Adj Close'].combine_first(df_full['Adj Close_sensex'])

        # Drop the extra column used for filling
        df_full.drop(columns=['Adj Close_sensex'], inplace=True)

        # For any remaining missing values, perform forward fill (in case some dates are not in the sensex data)
        df_full['Adj Close'].fillna(method='bfill', inplace=True)

        # Save the updated DataFrame to a new CSV file in the output directory
        output_filepath = os.path.join(output_dir, filename)
        df_full.to_csv(output_filepath, index=False)

        print(f"Processed and saved: {filename}")

print("All files have been processed and saved in the output directory.")