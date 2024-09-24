# main.py

from src.ingestion.data_ingestion import load_data, preprocess_data
from src.feature.adjust_light_timings import TrafficManager as LightTimingManager
from src.feature.traffic_simulation import TrafficManager as TrafficSimulationManager
from src.modeling.model_building import train_models
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    # Load and preprocess data
    data_path = 'Traffic_management_data.csv' 
    df = load_data(data_path)
    df = preprocess_data(df)

    # Adjust light timing
    light_manager = LightTimingManager(df)
    light_manager.adjust_light_timings()

    # Simulate traffic flow
    traffic_manager = TrafficSimulationManager(df)
    traffic_manager.simulate_traffic_flow()

    # Train models
    best_model, best_score = train_models(df)
    print(f"Best Model: {best_model} with accuracy {best_score:.2f}")

if __name__ == "__main__":
    main()
