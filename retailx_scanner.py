
# retailx_scanner.py

import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Data Loaded Successfully!")
    print(df.head())

if __name__ == "__main__":
    file_path = "sample_data.csv"
    load_data(file_path)
