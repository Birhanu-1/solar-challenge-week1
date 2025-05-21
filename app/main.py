import streamlit as st
import os
from utils import load_all_cleaned_data, plot_ghi_boxplot, display_top_regions


st.set_page_config(page_title="Solar GHI Dashboard", layout="centered")

st.title("☀️ Solar GHI Insights Dashboard")

# Load data
data = load_all_cleaned_data()

if not data:
    st.warning("No cleaned data found in '../data/data-clean'. Please check your files.")
    st.stop()

# Sidebar for country selection
country = st.sidebar.selectbox("Select Country", list(data.keys()))

df = data[country]

# Show GHI Boxplot
st.subheader(f"GHI Boxplot for {country.capitalize()}")
fig = plot_ghi_boxplot(df, country)
st.pyplot(fig)

# Show Top Regions
st.subheader(f"Top Regions by Average GHI in {country.capitalize()}")
top_n = st.slider("Select number of top regions to display", 3, 10, 5)
top_table = display_top_regions(df, top_n)
st.dataframe(top_table)
