

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib 
import os  
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
def train_models(df):
    """Train models and evaluate their accuracy."""
    X = df[['Traffic_Density', 'Vehicle_Count']]
    y = df['Light_Timing'].map({'Green': 0, 'Yellow': 1, 'Red': 2})

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'Logistic Regression': LogisticRegression(),
        'Random Forest': RandomForestClassifier()
    }

    best_model = None
    best_score = 0
    best_model_name = None

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"{name} Accuracy: {accuracy:.2f}")

        if accuracy > best_score:
            best_score = accuracy
            best_model = model
            best_model_name = name

    # Save the best model
    if best_model is not None:
        models_dir = 'models'
        os.makedirs(models_dir, exist_ok=True)  # Create the models directory if it doesn't exist
        model_path = os.path.join(models_dir, f"best_model_{best_model_name.replace(' ', '_')}.joblib")
        joblib.dump(best_model, model_path)  # Save the model
        print(f"Best model saved as: {model_path}")

    return best_model_name, best_score

if __name__ == "__main__":
    from ingestion.data_ingestion import load_data, preprocess_data

    # Load and preprocess data
    data_path = '../data/traffic_data.csv'
    df = load_data(data_path)
    df = preprocess_data(df)

    # Train models and get the best one
    best_model, best_score = train_models(df)
    print(f"Best Model: {best_model} with accuracy {best_score:.2f}")
