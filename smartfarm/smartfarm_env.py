# smartfarm_env.py

import pandas as pd
from datetime import datetime


def smartfarm_env():
    # Read the CSV file
    df = pd.read_csv('resampled1_smartfarmData_frGHNo1PlantGrow.csv')
    
    # Convert 'date' column to datetime format and store in a new 'Timestamp' column
    df['Timestamp'] = pd.to_datetime(df['date'])
    
    # Filter data up to the current timestamp
    current_time = datetime.now()
    filtered_df = df[df['Timestamp'] <= current_time]
    
    # Format 'Timestamp' to display as 'YYYY-MM-DD HR:MIN'
    filtered_df['Timestamp'] = filtered_df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M')
    
    # Select the first 15 columns, including 'Timestamp'
    selected_columns = ['Timestamp'] + [col for col in filtered_df.columns if col != 'date' and col != 'Timestamp'][:15]
    
    # Return only the selected columns in the filtered DataFrame
    return filtered_df[selected_columns]


