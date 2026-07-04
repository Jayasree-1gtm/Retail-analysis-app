import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Demand Forecasting")

# Load data
df = pd.read_csv("online_retail_cleaned-1.csv")

# Date conversion
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Monthly demand
monthly_demand = (
    df.groupby(df["InvoiceDate"].dt.to_period("M"))["Quantity"]
    .sum()
    .reset_index()
)

monthly_demand["InvoiceDate"] = monthly_demand["InvoiceDate"].astype(str)

# Forecast using moving average
forecast_value = monthly_demand["Quantity"].tail(3).mean()

forecast_df = pd.DataFrame({
    "InvoiceDate": ["Forecast"],
    "Quantity": [forecast_value]
})

combined = pd.concat([monthly_demand, forecast_df])

fig = px.line(
    combined,
    x="InvoiceDate",
    y="Quantity",
    title="Monthly Demand Forecast"
)

st.plotly_chart(fig, use_container_width=True)

st.metric(
    "Predicted Next Month Demand",
    f"{int(forecast_value):,} Units"
)

st.info("Forecast based on recent demand trend.")