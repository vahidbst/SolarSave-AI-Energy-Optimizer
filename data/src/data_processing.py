import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Load and preprocess solar energy data."""
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    df['weather'] = df['weather'].astype('category')
    return df.dropna()

if __name__ == "__main__":
    data = load_data("../data/sample_data.csv")
    print("Processed Data:")
    print(data.head())
