import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📦 Inventory Dashboard")

df = pd.read_csv("online_retail_cleaned-1.csv")

inventory = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig = px.bar(
    x=inventory.values,
    y=inventory.index,
    orientation="h",
    title="Top Products by Quantity Sold"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.histogram(
    df,
    x="Quantity",
    title="Inventory Distribution"
)

st.plotly_chart(fig, use_container_width=True)
