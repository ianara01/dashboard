# 스마트팜 습도 제어 클래스

class IoTsmartCoHumidity:
    def __init__(self, env_data, nutsol_data):
        self.env_data = env_data
        self.nutsol_data = nutsol_data
        self.control_actions = []

    def Humidity_Control(self):
        """습도 값에 따라 제어장치 On/Off하고, 'Humi'가 포함된 열을 찾아 각 습도에 맞게 제어합니다."""
        humidity_columns = [col for col in self.env_data.columns if "Humi" in col] + \
                           [col for col in self.nutsol_data.columns if "Humi" in col]

        actions = []

        # 각 습도 값에 대해 제어 수행
        for col in humidity_columns:
            if col in self.env_data.columns:
                humidity_value = self.env_data[col].iloc[0]
                timestamp = self.env_data['Timestamp'].iloc[0] if 'Timestamp' in self.env_data.columns else "Unknown"
            elif col in self.nutsol_data.columns:
                humidity_value = self.nutsol_data[col].iloc[0]
                timestamp = self.nutsol_data['Timestamp'].iloc[0] if 'Timestamp' in self.nutsol_data.columns else "Unknown"

            # 습도 조건에 따른 제어 작업 수행
            action = ""
            if humidity_value >= 75:
                action = f"{timestamp} - {col}: Dehumidifier ON / Vent_Fan ON (Humidity = {humidity_value}%)"
            elif 60 <= humidity_value < 75:
                action = f"{timestamp} - {col}: Dehumidifier OFF / Vent_Fan OFF (Humidity = {humidity_value}%)"
            elif humidity_value < 30:
                action = f"{timestamp} - {col}: Humidifier ON / Vent_Fan OFF (Humidity = {humidity_value}%)"
            elif 30 <= humidity_value < 50:
                action = f"{timestamp} - {col}: Humidifier OFF / Vent_Fan OFF (Humidity = {humidity_value}%)"
            elif 50 <= humidity_value < 60:
                action = f"{timestamp} - {col}: Vent_Fan OFF (Humidity = {humidity_value}%)"
            
            if action:
                self.control_actions.append(action)
                actions.append(action)

        return actions
