import pandas as pd
import streamlit as st

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def main():
    st.title("RetailX Smart Money Scanner")
    file_path = "sample_data.csv"
    
    try:
        df = load_data(file_path)
        st.success("Data Loaded Successfully!")
        st.dataframe(df)

        # Example: Basic Signal
        if 'Price' in df.columns and 'Volume' in df.columns:
            df['Signal'] = df.apply(lambda row: 'Buy' if row['Volume'] > 100000 and row['Price'] > 100 else 'Watch', axis=1)
            st.subheader("Generated Signals")
            st.dataframe(df[['Symbol', 'Price', 'Volume', 'Signal']])
        else:
            st.warning("Missing 'Price' or 'Volume' columns in data.")

    except Exception as e:
        st.error(f"Error loading data: {e}")

if __name__ == "__main__":
    main()
