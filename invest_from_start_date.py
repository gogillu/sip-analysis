import os
import pandas as pd

def process_file_old(file_path, start_date, output_dir):
    df = pd.read_csv(file_path)

    # Ensure the Date column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort the dataframe by Date just in case it's not sorted
    df = df.sort_values(by='Date')

    # Filter out rows with dates earlier than the start_date
    df = df[df['Date'] >= start_date]
    
    # Reset index to handle row positions
    df = df.reset_index(drop=True)
    
    # Find the index of the start_date and K-1 date
    if not df.empty and start_date in df['Date'].values:
        start_date_idx = df[df['Date'] == start_date].index[0]
        k_minus_1_idx = start_date_idx - 1
        
        if k_minus_1_idx >= 0:
            # Values from the K-1 row
            k_minus_1_cumulative_units = df.at[k_minus_1_idx, 'Cumulative Units Purchased']
            k_minus_1_total_invested = df.at[k_minus_1_idx, 'Total Invested']

            # Adjust values starting from the start_date row
            df.loc[start_date_idx:, 'Cumulative Units Purchased'] -= k_minus_1_cumulative_units
            df.loc[start_date_idx:, 'Total Invested'] -= k_minus_1_total_invested

            # Recalculate the Acquired Value
            df.loc[start_date_idx:, 'Acquired Value'] = df.loc[start_date_idx:, 'Cumulative Units Purchased'] * df.loc[start_date_idx:, 'Adj Close']

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the modified dataframe to a new CSV file
    output_file_name = os.path.join(output_dir, os.path.basename(file_path))
    df.to_csv(output_file_name, index=False)

def process_file(file_path, start_date, output_dir):
    df = pd.read_csv(file_path)

    # Ensure the Date column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort the dataframe by Date just in case it's not sorted
    df = df.sort_values(by='Date')

    # Find the index of the start_date in the sorted dataframe
    if not df.empty and pd.to_datetime(start_date) in df['Date'].values:
        start_date_idx = df[df['Date'] == pd.to_datetime(start_date)].index[0]

        # Find the index of the K-1 date
        k_minus_1_idx = start_date_idx - 1
        
        if k_minus_1_idx >= 0:
            # Values from the K-1 row
            k_minus_1_row = df.iloc[k_minus_1_idx]
            k_minus_1_cumulative_units = k_minus_1_row['Cumulative Units Purchased']
            k_minus_1_total_invested = k_minus_1_row['Total Invested']

            # Filter out rows with dates earlier than the start_date
            df_filtered = df[df['Date'] >= pd.to_datetime(start_date)]
            
            # Reset index to handle row positions
            df_filtered = df_filtered.reset_index(drop=True)
            
            # Adjust values starting from the start_date row
            df_filtered.loc[:, 'Cumulative Units Purchased'] -= k_minus_1_cumulative_units
            df_filtered.loc[:, 'Total Invested'] -= k_minus_1_total_invested
            
            # Recalculate the Acquired Value
            df_filtered['Acquired Value'] = df_filtered['Cumulative Units Purchased'] * df_filtered['Adj Close']

            # Create the output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Save the modified dataframe to a new CSV file
            output_file_name = os.path.join(output_dir, os.path.basename(file_path))
            df_filtered.to_csv(output_file_name, index=False)

def calculate_return_percentage(total_invested, acquired_value):
    """Calculate the return percentage based on total invested and acquired value."""
    return ((acquired_value - total_invested) * 100) / total_invested

def process_files_for_return_comparision(folder_path, market_last_day_value):
    """Process files in the given folder to calculate return percentages and save the results."""
    data = []

    for file_name in os.listdir(folder_path):
        if file_name.startswith('00_'):
            continue
        
        file_path = os.path.join(folder_path, file_name)
        
        # Read the last line of the file
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip().split(',')
                    if len(last_line) >= 7:  # Ensure there are enough columns
                        try:
                            # print(last_line,market_last_day_value)
                            total_invested = float(last_line[5])
                            acquired_value = float(last_line[4])*market_last_day_value
                            
                            return_percentage = calculate_return_percentage(total_invested, acquired_value)
                            
                            # Collect data
                            data.append({
                                'File Name': file_name,
                                'Total Invested': total_invested,
                                'Acquired Value': acquired_value,
                                'Return %': return_percentage
                            })
                        except ValueError:
                            print(f"Error parsing numerical values in file {file_name}")
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

    # Convert list to DataFrame
    df = pd.DataFrame(data)
    
    # Sort DataFrame by 'Return %' in descending order
    df_sorted = df.sort_values(by='Return %', ascending=False)
    
    # Save to CSV
    output_file = os.path.join(folder_path, '00_return_comparision.csv')
    df_sorted.to_csv(output_file, index=False)

def get_third_column_last_row(file_path):
    """
    Reads a CSV file and returns the value of the 3rd column in the last row.
    
    :param file_path: Path to the CSV file.
    :return: Value of the 3rd column of the last row.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Check if DataFrame is not empty
        if df.empty:
            raise ValueError("The CSV file is empty")
        
        # Get the value from the 3rd column of the last row
        last_row = df.iloc[-1]
        value = last_row[2]  # Index 2 for the 3rd column
        
        return value
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    start_date_str = '2014-11-01'
    start_date = pd.to_datetime(start_date_str)  # Replace with your desired start_date
    input_file = '10years/fine_tuned_daily_investment_with_all_dates_with_returns.csv'
    input_folder = '10years/fine_tuned_monthly_investment_schedules_with_units_all_dates_with_returns'
    output_folder = start_date.strftime('%Y-%m-%d')

    # Process the main input file
    process_file(input_file, start_date, output_folder)

    # Process all files in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        process_file(file_path, start_date, output_folder)

    market_last_day_value = float(get_third_column_last_row(input_file))
    print("mld",market_last_day_value)
    process_files_for_return_comparision(start_date_str,market_last_day_value)

if __name__ == '__main__':
    main()