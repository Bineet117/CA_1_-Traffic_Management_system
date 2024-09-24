# src/feature/adjust_light_timing.py

class TrafficManager:
    def __init__(self, df):
        self.df = df

    def adjust_light_timings(self):
        for index, row in self.df.iterrows():
            density = row['Traffic_Density']
            if density > 0.7:
                self.df.at[index, 'Light_Timing'] = 'Green'
            elif 0.3 < density <= 0.7:
                self.df.at[index, 'Light_Timing'] = 'Yellow'
            else:
                self.df.at[index, 'Light_Timing'] = 'Red'
