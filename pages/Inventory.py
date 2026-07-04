import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📦 Inventory Dashboard")

df = pd.read_csv("online_retail_cleaned_small.csv")

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

st.subheader("Inventory Distribution")

inventory_dist = (
    df.groupby("Description")["Quantity"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

fig = px.bar(
    x=inventory_dist.index,
    y=inventory_dist.values,
    labels={"x": "Product", "y": "Quantity"},
    title="Top 10 Products Inventory Distribution"
)

st.plotly_chart(fig, use_container_width=True)
