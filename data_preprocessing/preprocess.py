# data_preprocessing/preprocess.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess(transaction):
    # Convert to DataFrame for easier processing
    df = pd.DataFrame([transaction])
    
    # Feature Engineering
    df['hour'] = pd.to_datetime(df['timestamp'], unit='s').dt.hour
    df['is_high_value'] = df['amount'] > 500
    
    # Scaling numerical features
    scaler = StandardScaler()
    df[['amount']] = scaler.fit_transform(df[['amount']])
    
    return df
