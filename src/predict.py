import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from weather_api import get_weather_data

def clean_data(df):
    """تمیزکاری و تبدیل داده‌ها"""
    # تبدیل ستون‌های عددی
    numeric_cols = ['temperature', 'panel_angle', 'energy_kwh']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # تبدیل متن به NaN
    
    # تبدیل وضعیت آب‌وهوا
    weather_map = {'Sunny': 2, 'Cloudy': 1, 'Rainy': 0}
    df['weather'] = df['weather'].map(weather_map)
    
    # حذف ردیف‌های نامعتبر
    df = df.dropna()
    
    # تبدیل نهایی به نوع داده صحیح
    df = df.astype({
        'panel_angle': 'int32',
        'weather': 'int32'
    })
    
    return df

def train_model(data_path: str, api_key: str = None):
    try:
        # خواندن و تمیزکردن داده‌ها
        df = pd.read_csv(data_path)
        df = clean_data(df)
        
        if len(df) < 5:
            raise ValueError(f"تنها {len(df)} نمونه معتبر وجود دارد. حداقل به ۵ نمونه نیاز است.")
        
        # آموزش مدل
        X = df[['panel_angle', 'temperature', 'weather']]
        y = df['energy_kwh']
        
        model = RandomForestRegressor(n_estimators=100)
        model.fit(X, y)
        
        print(f"Model trained successfully! (R²): {model.score(X, y):.2f}")
        return model
    
    except Exception as e:
        print(f"خطا: {e}")
        return None

if __name__ == "__main__":
    model = train_model(
        data_path="data/sample_data.csv",
        api_key="6a0431544ae322ea88178ece77016b05"  # کلید واقعی خود را وارد کنید
    )
