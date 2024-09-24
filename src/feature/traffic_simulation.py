# src/feature/traffic_simulation.py

class TrafficManager:
    def __init__(self, df):
        self.df = df

    def simulate_traffic_flow(self):
        """Simulate traffic flow at the intersection."""
        for index, row in self.df.iterrows():
            vehicles_passed = 0
            if row['Light_Timing'] == 'Green':
                vehicles_passed = min(row['Vehicle_Count'], 60)
            elif row['Light_Timing'] == 'Yellow':
                vehicles_passed = min(row['Vehicle_Count'], 20)
            print(f"At {row['Time']}, {vehicles_passed} vehicles passed during {row['Light_Timing']} light.")
