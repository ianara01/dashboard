# 스마트팜 온도 제어 클래스

class IoTsmartCoTemp:
    def __init__(self, env_data, nutsol_data):
        self.env_data = env_data
        self.nutsol_data = nutsol_data
        self.control_actions = []
    
    def Temp_Control(self):
        """온도 값에 따라 제어장치 On/Off하고, 'Temp'가 포함된 열을 찾아 각 온도에 맞게 제어합니다."""
        temp_columns = [col for col in self.env_data.columns if "Temp" in col] + \
                       [col for col in self.nutsol_data.columns if "Temp" in col]

        actions = []

        # 각 온도 값에 대해 제어 수행
        for col in temp_columns:
            if col in self.env_data.columns:
                temp_value = self.env_data[col].iloc[0]
                timestamp = self.env_data['Timestamp'].iloc[0] if 'Timestamp' in self.env_data.columns else "Unknown"
            elif col in self.nutsol_data.columns:
                temp_value = self.nutsol_data[col].iloc[0]
                timestamp = self.nutsol_data['Timestamp'].iloc[0] if 'Timestamp' in self.nutsol_data.columns else "Unknown"

            # 온도 조건에 따른 제어 작업 수행
            action = ""
            if temp_value > 28:
                action = f"{timestamp} - {col}: Air_Conditioner ON (Temperature = {temp_value})"
            elif 25 <= temp_value <= 28:
                action = f"{timestamp} - {col}: Air_Conditioner OFF (Temperature = {temp_value})"
            elif temp_value < 10:
                action = f"{timestamp} - {col}: Heater ON (Temperature = {temp_value})"
            elif 18 <= temp_value < 25:
                action = f"{timestamp} - {col}: Heater OFF (Temperature = {temp_value})"
            
            if action:
                self.control_actions.append(action)
                actions.append(action)
                
        return actions

