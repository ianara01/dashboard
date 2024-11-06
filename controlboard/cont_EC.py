# Smart Farm EC Control

class IoTsmartCoEC:
    def __init__(self, env_data, nutsol_data):
        self.env_data = env_data
        self.nutsol_data = nutsol_data
        self.control_actions = []

    def EC_Control(self):
        """EC 값에 따라 제어장치를 On/Off하고, 'EC'가 포함된 열을 찾아 각 EC 값에 맞게 제어합니다."""
        ec_columns = [col for col in self.env_data.columns if "EC" in col] + \
                     [col for col in self.nutsol_data.columns if "EC" in col]

        actions = []

        # 각 EC 값에 대해 제어 수행
        for col in ec_columns:
            if col in self.env_data.columns:
                ec_value = self.env_data[col].iloc[0]
                timestamp = self.env_data['Timestamp'].iloc[0] if 'Timestamp' in self.env_data.columns else "Unknown"
            elif col in self.nutsol_data.columns:
                ec_value = self.nutsol_data[col].iloc[0]
                timestamp = self.nutsol_data['Timestamp'].iloc[0] if 'Timestamp' in self.nutsol_data.columns else "Unknown"

            # EC 조건에 따른 제어 작업 수행
            action = ""
            if ec_value > 3.0:
                action = f"{timestamp} - {col}: Supply H2O or Nutrient C (EC = {ec_value})"
            elif 1.8 <= ec_value <= 3.0:
                action = f"{timestamp} - {col}: Stop H2O and Nutrient C Supply (EC = {ec_value})"
            elif ec_value < 0.5:
                action = f"{timestamp} - {col}: Supply Nutrients A and B (EC = {ec_value})"
            elif 0.5 <= ec_value < 1.5:
                action = f"{timestamp} - {col}: Stop Nutrients A and B Supply (EC = {ec_value})"
            
            if action:
                self.control_actions.append(action)
                actions.append(action)

        return actions
