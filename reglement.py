import streamlit as st
import polars as pl

@st.cache_data
def load_data():
    df = pl.read_csv("individuals_with_descriptions.csv")
    return df

df = load_data()

# Dropdown 1: e.g. countries
options_1 = df.select("country").unique().to_series().to_list()
selection_1 = st.selectbox("Choose country", options_1)

# Filter only when selection is made
filtered_df = df.filter(pl.col("country") == selection_1)

# Dropdown 2: e.g. cities in that country
options_2 = filtered_df.select("city").unique().to_series().to_list()
selection_2 = st.selectbox("Choose city", options_2)

selected_text = df.filter((pl.col("city")== selection_2 )& (pl.col("country")== selection_1))[0, "description"]
st.write(selected_text)
