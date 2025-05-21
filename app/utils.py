import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_all_cleaned_data(data_dir="data"):
    all_data = {}
    if not os.path.exists(data_dir):
        return all_data
    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            path = os.path.join(data_dir, file)
            try:
                df = pd.read_csv(path)
                country = file.replace(".csv", "")
                all_data[country] = df
            except Exception as e:
                print(f"Error loading {file}: {e}")
    return all_data

def plot_ghi_boxplot(df, country):
    plt.figure(figsize=(8, 5))
    sns.boxplot(y=df['GHI'])  # Assuming column is named 'GHI'
    plt.title(f"GHI Distribution - {country.capitalize()}")
    plt.ylabel("GHI (kWh/m²)")
    plt.tight_layout()
    return plt.gcf()

def display_top_regions(df, top_n=5):
    if 'Region' not in df.columns or 'GHI' not in df.columns:
        return pd.DataFrame()
    return df.groupby("Region")["GHI"].mean().sort_values(ascending=False).head(top_n).reset_index()
