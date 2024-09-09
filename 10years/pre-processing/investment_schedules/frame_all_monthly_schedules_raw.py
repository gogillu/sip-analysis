import pandas as pd
import os

# Load the original investment schedule
df = pd.read_csv('monthly_on_1_investment_schedule.csv', parse_dates=['Date'])

# Ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create a directory to store the files if it doesn't exist
output_dir = "monthly_investment_schedules"
os.makedirs(output_dir, exist_ok=True)

# Iterate through the days 1 to 28
for i in range(1, 29):
    # Create a copy of the original DataFrame
    df_i = df.copy()
    
    # Adjust the day to the ith day of the month
    df_i['Date'] = df_i['Date'].apply(lambda x: x.replace(day=i) if pd.Timestamp(x.year, x.month, i).is_month_end == False else x.replace(day=x.days_in_month))

    # Save the transformed data to the corresponding CSV file
    file_name = f'monthly_on_{i}_investment_schedule.csv'
    df_i.to_csv(os.path.join(output_dir, file_name), index=False)

print(f"28 files saved in the '{output_dir}' directory.")