# SmartFarm Integrated Monitoring과 SmartFarm AIoT Control Monitoringt을 함께 표현하고 AIoT 제어

import pandas as pd
import time
import streamlit as st
from smartfarm.smartfarm_env import smartfarm_env
from smartfarm.smartfarm_nutsol import smartfarm_nutsol
from smartfarm.smartfarm_plantgrow import smartfarm_plantgrow
from smartfarm.display_env_data import display_env_data
from smartfarm.display_nutsol_data import display_nutsol_data
from smartfarm.display_plantgrow_data import display_plantgrow_data
from dashboard.cont_temp import IoTsmartCoTemp
from dashboard.cont_humid import IoTsmartCoHumidity
from dashboard.cont_pH import IoTsmartCopH
from dashboard.cont_EC import IoTsmartCoEC

# Set up Streamlit layout
st.title("SmartFarm Monitoring and Control")

# Sidebar for choosing between Integrated Monitoring and AIoT Control Monitoring
main_option = st.sidebar.selectbox("Choose Monitoring Type", 
                                  ("SmartFarm Integrated Monitoring", "SmartFarm AIoT Control Monitoring"))

def main():
    if main_option == "SmartFarm Integrated Monitoring":
        st.subheader("Integrated Monitoring Dashboard")
        sub_option = st.sidebar.selectbox("Choose Monitoring Type", 
                                          ("Environment Monitoring", "Nutrient Solution Monitoring", "Plant Growth Monitoring"))
        
        # Handling Integrated Monitoring data
        if sub_option == "Environment Monitoring":
            st.header("Environment Monitoring")
            env_data = smartfarm_env()
            if isinstance(env_data, pd.DataFrame):
                display_env_data(env_data)
            else:
                st.write(env_data)
        
        elif sub_option == "Nutrient Solution Monitoring":
            st.header("Nutrient Solution Monitoring")
            nutsol_data = smartfarm_nutsol()
            if isinstance(nutsol_data, pd.DataFrame):
                display_nutsol_data(nutsol_data)
            else:
                st.write(nutsol_data)
        
        elif sub_option == "Plant Growth Monitoring":
            st.header("Plant Growth Monitoring")
            plantgrow_data = smartfarm_plantgrow()
            if isinstance(plantgrow_data, pd.DataFrame):
                display_plantgrow_data(plantgrow_data)
            else:
                st.write(plantgrow_data)
    
    elif main_option == "SmartFarm AIoT Control Monitoring":
        st.subheader("AIoT Control Monitoring Dashboard")
        control_option = st.sidebar.selectbox("Choose Control Type", 
                                             ("Temp Control Panel", "Humidity Control Panel", 
                                              "EC Control Panel", "pH Control Panel", "Growth Control Panel"))
        
        # Calling the function to handle AIoT control
        header_text, actions, env_data, nutsol_data = cont_main(control_option)

        st.header(header_text)

        st.subheader("Environment Data")
        st.write(env_data)

        st.subheader("Nutrient Solution Data")
        st.write(nutsol_data)

        st.subheader("Control Actions")
        for action in actions:
            st.write(action)


def cont_main(control_option):
    """Handles control actions based on the selected control option."""
    header_text = ""
    controller_actions = []

    # Load data
    env_data = smartfarm_env()
    nutsol_data = smartfarm_nutsol()

    # Initialize the IoT controller for control options
    temperature_controller = IoTsmartCoTemp(env_data, nutsol_data)
    humidity_controller = IoTsmartCoHumidity(env_data, nutsol_data)
    pH_controller = IoTsmartCopH(env_data, nutsol_data)
    EC_controller = IoTsmartCoEC(env_data, nutsol_data)

    # Assign the correct controller and header text based on selected option
    if control_option == "Temp Control Panel":
        header_text = "Temperature Monitoring and Control"
        controller_actions = temperature_controller.Temp_Control()
    
    elif control_option == "Humidity Control Panel":
        header_text = "Humidity Control"
        # Implement corresponding control for humidity
        controller_actions = humidity_controller.Humidity_Control()
    
    elif control_option == "EC Control Panel":
        header_text = "EC Control"
        # Implement corresponding control for EC
        controller_actions = EC_controller.EC_Control()
    
    elif control_option == "pH Control Panel":
        header_text = "pH Control"
        # Implement corresponding control for pH
        controller_actions = pH_controller.pH_Control()

    elif control_option == "Growth Control Panel":
        header_text = "Growth Control"
        # Implement corresponding control for plant growth
        # controller_actions = growth_controller.Growth_Control()

    return header_text, controller_actions, env_data, nutsol_data

# Run the main function to display the dashboard
main()
