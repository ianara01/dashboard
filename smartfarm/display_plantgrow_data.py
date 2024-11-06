# Display Plant Growth

import time
import streamlit as st
import pandas as pd

def display_plantgrow_data(plantgrow_data):
    """Display Plant Growth Data by Group with a delay, including timestamp if available."""
    group1 = ["GHa01_height", "GHb01_height", "GHb02_height", "GHb03_height", "GHc01_height"]
    group2 = ["GHc02_height", "GHc03_height", "GHd01_height", "GHd02_height", "GHd03_height"]
    group3 = ["GHe01_height", "GHe02_height", "GHe03_height", "GHf01_height", "GHf03_height"]

    # Create placeholders for each group to update independently
    placeholder1 = st.empty()
    placeholder2 = st.empty()
    placeholder3 = st.empty()
    
    # Extract each group data with timestamp
    group1_data = plantgrow_data[group1]
    group2_data = plantgrow_data[group2]
    group3_data = plantgrow_data[group3]
    
    # Insert timestamp if it exists
    if 'Timestamp' in plantgrow_data.columns:
        group1_data.insert(0, 'Timestamp', plantgrow_data['Timestamp'])
        group2_data.insert(0, 'Timestamp', plantgrow_data['Timestamp'])
        group3_data.insert(0, 'Timestamp', plantgrow_data['Timestamp'])
    
    # Determine the maximum number of rows across groups
    max_rows = max(len(group1_data), len(group2_data), len(group3_data))
    
    # Iterate through rows for each group simultaneously
    for i in range(max_rows):
        with placeholder1.container():
            if i < len(group1_data):
                st.subheader("Plant Growth Group 1")
                st.write(group1_data.iloc[i].to_frame().T)
        
        with placeholder2.container():
            if i < len(group2_data):
                st.subheader("Plant Growth Group 2")
                st.write(group2_data.iloc[i].to_frame().T)
        
        with placeholder3.container():
            if i < len(group3_data):
                st.subheader("Plant Growth Group 3")
                st.write(group3_data.iloc[i].to_frame().T)
        
        # Short sleep to update rows simultaneously across groups
        time.sleep(3)
