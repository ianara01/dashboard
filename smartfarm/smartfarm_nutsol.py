# smartfarm_nutsol.py

import pandas as pd
from datetime import datetime

def smartfarm_nutsol():
    # Read the CSV file
    df = pd.read_csv('resampled1_smartfarmData_frGHNo1PlantGrow.csv')
    
    # Convert 'date' column to datetime format if not already done
    df['Timestamp'] = pd.to_datetime(df['date'])    
    
    # Filter data up to the current timestamp
    current_time = datetime.now()
    filtered_df = df[df['Timestamp'] <= current_time]
    
    # Create a list of columns excluding 'date'
    remaining_columns = [col for col in filtered_df.columns if col != 'date']
    
    # Ensure 'Timestamp' is included and select from the remaining columns (16 to 25)
    if 'Timestamp' in remaining_columns:
        # Get the index of 'Timestamp' for the output
        selected_columns = ['Timestamp'] + remaining_columns[15:25]
    else:
        # If for any reason 'Timestamp' is not in the columns (shouldn't be the case here)
        selected_columns = remaining_columns[15:25]

    # Return only the selected columns in the filtered DataFrame
    return filtered_df[selected_columns]

