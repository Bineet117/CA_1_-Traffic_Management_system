# src/ingestion/data_ingestion.py

import pandas as pd

def load_data(file_path):
    """Load the traffic data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """Preprocess the DataFrame."""
    df.dropna(inplace=True)  # Drop rows with missing values
    return df

s = load_data("Traffic_management_data.csv")
print(s.head())