# create data.py...
import pandas as pd

# Load the provided file with 2023 readings
file_path_2023 = 'path_to_your_2023_csv_file.csv'
df_2023 = pd.read_csv(file_path_2023)

# Convert 'Reading' column to numeric and 'Date' column to datetime
df_2023['Reading'] = pd.to_numeric(df_2023['Reading'], errors='coerce').fillna(0)
df_2023['Date'] = pd.to_datetime(df_2023['Date'])

# Define the years for the 7 previous readings
years = [2023, 2020, 2017, 2014, 2011, 2008, 2005]

# Initialize an empty dataframe to store the combined data
combined_df = pd.DataFrame()

# Iterate over each year and create the data
for i, year in enumerate(years):
    # Copy the 2023 data
    new_df = df_2023.copy()

    # Update the 'Date' column to the current year
    new_df['Date'] = new_df['Date'].apply(lambda x: x.replace(year=year))

    # Increment readings based on the year difference from 2023
    new_df['Reading'] = new_df['Reading'] + (2023 - year)

    # Append to the combined dataframe
    combined_df = pd.concat([combined_df, new_df])

# Sort the final combined dataframe by date in ascending order
combined_df = combined_df.sort_values(by='Date', ascending=True)

# Save the final combined dataframe to a CSV file
combined_df.to_csv('final_combined_file_path.csv', index=False)
