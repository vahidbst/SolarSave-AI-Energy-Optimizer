import pandas as pd
from weather_api import get_weather_data  # اضافه کردن ایمپورت

def load_data(filepath: str, api_key: str = None) -> pd.DataFrame:
    """Load data and optionally fetch live weather."""
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    
    if api_key:
        weather = get_weather_data(api_key)
        # اضافه کردن داده‌های آب‌وهوا به دیتافریم
        df.loc[0, 'temperature'] = weather['temperature']
        df.loc[0, 'weather'] = weather['condition']
    
    return df.dropna()

if __name__ == "__main__":
    data = load_data("../data/sample_data.csv", api_key="6a0431544ae322ea88178ece77016b05")  # کلید خود را وارد کنید
    print("Data with Live Weather:")
    print(data.head())