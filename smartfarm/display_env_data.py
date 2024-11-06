# 환경 Display Environment Variables

import pandas as pd
import time
import streamlit as st


def display_env_data(env_data):
    """Display Environment Data for all groups simultaneously with independent row updates."""
    group1 = ["UV", "exTemp", "exHumid", "Win_dir", "Win_speed"]
    group2 = ["Temp_inL(F)", "Temp_inL(C)", "Temp_inH(F)", "Temp_inH(C)", "Humi_inL(F)"]
    group3 = ["Humi_inL(C)", "Humi_inH(F)", "Humi_inH(C)", "heater_1", "CirFan"]

    # Create placeholders for each group to update independently
    placeholder1 = st.empty()
    placeholder2 = st.empty()
    placeholder3 = st.empty()
    
    # Extract each group data with timestamp
    group1_data = env_data[group1]
    group2_data = env_data[group2]
    group3_data = env_data[group3]
    
    # Insert timestamp if it exists
    if 'Timestamp' in env_data.columns:
        group1_data.insert(0, 'Timestamp', env_data['Timestamp'])
        group2_data.insert(0, 'Timestamp', env_data['Timestamp'])
        group3_data.insert(0, 'Timestamp', env_data['Timestamp'])
    
    # Determine the maximum number of rows across groups
    max_rows = max(len(group1_data), len(group2_data), len(group3_data))
    
    # Iterate through rows for each group simultaneously
    for i in range(max_rows):
        with placeholder1.container():
            if i < len(group1_data):
                st.subheader("Environment Group 1")
                st.write(group1_data.iloc[i].to_frame().T)
        
        with placeholder2.container():
            if i < len(group2_data):
                st.subheader("Environment Group 2")
                st.write(group2_data.iloc[i].to_frame().T)
        
        with placeholder3.container():
            if i < len(group3_data):
                st.subheader("Environment Group 3")
                st.write(group3_data.iloc[i].to_frame().T)
        
        # Short sleep to update rows simultaneously across groups
        time.sleep(1)

