# Smart Farm pH Control

class IoTsmartCopH:
    def __init__(self, env_data, nutsol_data):
        self.env_data = env_data
        self.nutsol_data = nutsol_data
        self.control_actions = []

    def pH_Control(self):
        """pH 값에 따라 제어장치 On/Off하고, 'pH'가 포함된 열을 찾아 각 pH 값에 맞게 제어합니다."""
        ph_columns = [col for col in self.env_data.columns if "pH" in col] + \
                     [col for col in self.nutsol_data.columns if "pH" in col]

        actions = []

        # 각 pH 값에 대해 제어 수행
        for col in ph_columns:
            if col in self.env_data.columns:
                ph_value = self.env_data[col].iloc[0]
                timestamp = self.env_data['Timestamp'].iloc[0] if 'Timestamp' in self.env_data.columns else "Unknown"
            elif col in self.nutsol_data.columns:
                ph_value = self.nutsol_data[col].iloc[0]
                timestamp = self.nutsol_data['Timestamp'].iloc[0] if 'Timestamp' in self.nutsol_data.columns else "Unknown"

            # pH 조건에 따른 제어 작업 수행
            action = ""
            if ph_value > 7.6:
                action = f"{timestamp} - {col}: Nitric Acid or Phosphoric Acid ON / Nutrient D ON (pH = {ph_value})"
            elif 6.8 <= ph_value <= 7.6:
                action = f"{timestamp} - {col}: Acid OFF / Nutrient D OFF (pH = {ph_value})"
            elif ph_value < 5.0:
                action = f"{timestamp} - {col}: NaOH ON / Nutrient B ON (pH = {ph_value})"
            elif 5.0 <= ph_value < 6.5:
                action = f"{timestamp} - {col}: NaOH OFF / Nutrient B OFF (pH = {ph_value})"
            elif 6.5 <= ph_value < 6.8:
                action = f"{timestamp} - {col}: Control OFF (pH = {ph_value})"
            
            if action:
                self.control_actions.append(action)
                actions.append(action)

        return actions
