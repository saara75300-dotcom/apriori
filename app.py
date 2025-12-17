!pip install streamlit

import streamlit as st
import pandas as pd
import pickle

st.set_page_config(layout="wide")

st.title("Apriori Association Rules")

# Define the path to the pickle file
pickle_path = "/content/drive/MyDrive/apriori_final_metrics.pkl"

# Load the association rules from the pickle file
try:
    with open(pickle_path, 'rb') as file:
        rules = pickle.load(file)
    st.success("Association rules loaded successfully!")
except FileNotFoundError:
    st.error(f"Error: The file '{pickle_path}' was not found. Please ensure it's uploaded to your Google Drive and the path is correct.")
    rules = pd.DataFrame()

if not rules.empty:
    st.write("Here are the generated association rules:")
    st.dataframe(rules)

    st.subheader("Filter Rules")
    min_support = st.slider("Minimum Support", min_value=0.0, max_value=1.0, value=rules['support'].min(), step=0.01)
    min_confidence = st.slider("Minimum Confidence", min_value=0.0, max_value=1.0, value=rules['confidence'].min(), step=0.01)
    min_lift = st.slider("Minimum Lift", min_value=0.0, max_value=rules['lift'].max(), value=rules['lift'].min(), step=0.01)

    filtered_rules = rules[
        (rules['support'] >= min_support) &
        (rules['confidence'] >= min_confidence) &
        (rules['lift'] >= min_lift)
    ]

    if not filtered_rules.empty:
        st.write("Filtered Association Rules:")
        st.dataframe(filtered_rules)
    else:
        st.warning("No rules found matching the selected filters.")
else:
    st.info("No rules to display. Please check if the pickle file was generated correctly.")
