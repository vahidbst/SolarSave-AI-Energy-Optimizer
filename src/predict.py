import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def train_model(data_path: str):
    """Train a simple energy prediction model."""
    df = pd.read_csv(data_path)
    X = df[['panel_angle', 'temperature']]
    y = df['energy_kwh']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    
    print(f"Model trained! Test Score: {model.score(X_test, y_test):.2f}")
    return model

if __name__ == "__main__":
    model = train_model("../data/sample_data.csv")
