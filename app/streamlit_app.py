import streamlit as st
import pandas as pd
import os

# Set page configuration
st.set_page_config(page_title="Inventory Optimization", layout="wide")

# Title
st.title("📊 Inventory Optimization Dashboard")

# Load the optimized inventory data
file_path = "C:/Users/user/Desktop/DA/outputs/optimized_inventory.csv"
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    st.success("Data loaded successfully!")
else:
    st.error("Optimized inventory file not found!")
    st.stop()


# Check if required columns exist
required_columns = ["date", "predicted_sales", "optimal_inventory"]
if all(col in data.columns for col in required_columns):
    # Display the data
    st.subheader("📋 Optimized Inventory Data")
    st.dataframe(data)


    # Interactive date filter
    st.subheader("📅 Filter Data by Date Range")
    start_date = st.date_input("Start Date", pd.to_datetime(data["date"]).min())
    end_date = st.date_input("End Date", pd.to_datetime(data["date"]).max())

    # Filter data based on selected date range
    data_filtered = data[
        (pd.to_datetime(data["date"]) >= pd.to_datetime(start_date)) &
        (pd.to_datetime(data["date"]) <= pd.to_datetime(end_date))
    ]

    st.write(f"Showing data from {start_date} to {end_date}:")

    # Line chart for predicted vs. optimized inventory (filtered data)
    st.subheader("📈 Predicted vs Optimized Inventory")
    st.line_chart(data_filtered.set_index("date")[["predicted_sales", "optimal_inventory"]])



    # Download option for the filtered data
    st.subheader("💾 Download Filtered Data")
    csv = data_filtered.to_csv(index=False)
    st.download_button(
        label="Download Filtered CSV",
        data=csv,
        file_name="optimized_inventory_filtered.csv",
        mime="text/csv",
    )
else:
    st.error(f"Required columns missing: {set(required_columns) - set(data.columns)}")


