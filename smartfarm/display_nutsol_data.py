# Display Nutrien Solution

import time
import streamlit as st
import pandas as pd

def display_nutsol_data(nutsol_data):
    """Display Nutrient Solution Data by Group with a delay, including timestamp if available."""
    group1 = ["Insolation", "NutSol_Temp", "NutSol_EC", "NutSol_pH", "NutSol_inTemp"]
    group2 = ["NutSol_exTemp", "NutSol_inHumid", "NutSol_exHumid", "NutSol_Insolatn", "NutSol_UV"]
    group3 = []
    
    # Create placeholders for each group to update independently
    placeholder1 = st.empty()
    placeholder2 = st.empty()
    placeholder3 = st.empty()

    # Extract each group data with timestamp
    group1_data = nutsol_data[group1]
    group2_data = nutsol_data[group2]
    group3_data = nutsol_data[group3]

    # Insert timestamp if it exists
    if 'Timestamp' in nutsol_data.columns:
        group1_data.insert(0, 'Timestamp', nutsol_data['Timestamp'])
        group2_data.insert(0, 'Timestamp', nutsol_data['Timestamp'])
        group3_data.insert(0, 'Timestamp', nutsol_data['Timestamp'])
    
    # Determine the maximum number of rows across groups
    max_rows = max(len(group1_data), len(group2_data), len(group3_data))

    # Iterate through rows for each group simultaneously
    for i in range(max_rows):
        with placeholder1.container():
            if i < len(group1_data):
                st.subheader("Nutrient Solution Group 1")
                st.write(group1_data.iloc[i].to_frame().T)
        
        with placeholder2.container():
            if i < len(group2_data):
                st.subheader("Nutrient Solution Group 2")
                st.write(group2_data.iloc[i].to_frame().T)

        with placeholder3.container():
            if i < len(group3_data):
                st.subheader("Nutrient Solution Group 3")
                st.write(group3_data.iloc[i].to_frame().T)
        # Short sleep to update rows simultaneously across groups
        time.sleep(2)
