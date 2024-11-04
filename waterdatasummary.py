import streamlit as st
import pandas as pd
import numpy as np
# ChatGPT was used for coding help
st.title("Water Quality Data Uploader and Summary")
st.write("Upload a CSV file with water quality data.")

# Upload data
uploaded_file = st.file_uploader("Upload your water quality dataset (CSV)", type=["csv"])
if uploaded_file:
    # Load the data
    df = pd.read_csv(uploaded_file)

    # Convert relevant columns to numeric, forcing errors to NaN
    for col in ['pH Level', 'Turbidity (NTU)', 'Nitrate Levels (mg/L)', 'Dissolved Oxygen (mg/L)']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Display raw data
    st.write("### Uploaded Data Preview")
    st.write(df.head())

    # Data Summary
    st.write("### Data Summary")
    st.write(df.describe())

    # Step 4: Summarize Key Insights
    avg_ph = df['pH Level'].mean() if 'pH Level' in df.columns else "N/A"
    avg_turbidity = df['Turbidity (NTU)'].mean() if 'Turbidity (NTU)' in df.columns else "N/A"
    avg_nitrate = df['Nitrate Levels (mg/L)'].mean() if 'Nitrate Levels (mg/L)' in df.columns else "N/A"
    avg_dissolved_oxygen = df['Dissolved Oxygen (mg/L)'].mean() if 'Dissolved Oxygen (mg/L)' in df.columns else "N/A"

    st.write("### Key Water Quality Metrics")
    st.write(f"- **Average pH**: {avg_ph}")
    st.write(f"- **Average Turbidity (NTU)**: {avg_turbidity}")
    st.write(f"- **Average Nitrate (mg/L)**: {avg_nitrate}")
    st.write(f"- **Average Dissolved Oxygen (mg/L)**: {avg_dissolved_oxygen}")

    # Warnings based on thresholds
    if isinstance(avg_ph, float):  # Check if avg_ph is a float before comparison
        if avg_ph < 6.5 or avg_ph > 8.5:
            st.warning("Warning: The average pH level is outside of the safe drinking water range (6.5-8.5).")
    if isinstance(avg_nitrate, float):  # Check if avg_nitrate is a float before comparison
        if avg_nitrate > 10:
            st.warning("Warning: Average nitrate level exceeds the safe limit for drinking water (10 mg/L).")

    # Optional: Visualization of pH levels over time
    if 'Date' in df.columns:
        st.write("### Time Series of pH Levels")
        st.line_chart(df.set_index('Date')['pH Level'])

    

   
