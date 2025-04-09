import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from weather_api import get_weather_data  # Import weather data

def train_model(data_path: str, api_key: str = None):
    """Train model with weather integration"""
    df = pd.read_csv(data_path)
    
    # Add live weather if API key provided
    if api_key:
        weather = get_weather_data(api_key)
        df.loc[0, 'temperature'] = weather['temperature']
        df.loc[0, 'weather'] = weather['condition']
    
    # Convert weather to numerical values
    df['weather'] = df['weather'].map({'Sunny': 2, 'Cloudy': 1, 'Rainy': 0})
    
    # Features and Target
    X = df[['panel_angle', 'temperature', 'weather']]
    y = df['energy_kwh']
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    
    print(f"Model trained! Accuracy: {model.score(X_test, y_test):.2f}")
    return model

if __name__ == "__main__":
    model = train_model(
        data_path="../data/sample_data.csv",
        api_key="your_api_key"  # Replace with your key
    )
