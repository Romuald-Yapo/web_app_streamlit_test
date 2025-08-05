import streamlit as st
import polars as pl

# Sample Polars DataFrame
data = pl.DataFrame({
    "Id": [1, 1, 2, 2, 3],
    "text_title": ["Intro", "Conclusion", "Overview", "Details", "Summary"],
    "text": [
        "This is the introduction of ID 1.",
        "This is the conclusion of ID 1.",
        "Overview of ID 2 is here.",
        "Detailed content for ID 2.",
        "Summary of ID 3 goes here."
    ]
})

st.title("Text Viewer App (Polars)")

# Convert to pandas for Streamlit dropdown compatibility
df_pd = data.to_pandas()

# First dropdown: Select ID
selected_id = st.selectbox("Select an ID", sorted(df_pd["Id"].unique()))

# Filter titles based on selected ID
filtered_titles = df_pd[df_pd["Id"] == selected_id]["text_title"].tolist()

# Second dropdown: Select a text_title
selected_title = st.selectbox("Select a Text Title", filtered_titles)

# Get corresponding text
selected_text = df_pd[
    (df_pd["Id"] == selected_id) & (df_pd["text_title"] == selected_title)
]["text"].values[0]

# Display text
st.subheader("Text Content")
st.write(selected_text)
