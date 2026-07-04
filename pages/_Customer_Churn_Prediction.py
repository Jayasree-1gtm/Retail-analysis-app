import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚠️ Customer Churn Prediction")

# Load data
df = pd.read_csv("online_retail_cleaned-1.csv")

# Calculate customer sales
customer_sales = df.groupby("CustomerID")["Sales"].sum().reset_index()

# Simple churn rule
avg_sales = customer_sales["Sales"].mean()

customer_sales["Status"] = customer_sales["Sales"].apply(
    lambda x: "At Risk" if x < avg_sales else "Active"
)

# KPI Cards
active = (customer_sales["Status"] == "Active").sum()
at_risk = (customer_sales["Status"] == "At Risk").sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("🟢 Active Customers", active)

with col2:
    st.metric("🔴 At Risk Customers", at_risk)

# Churn Chart
status_count = customer_sales["Status"].value_counts()

fig = px.bar(
    x=status_count.index,
    y=status_count.values,
    title="Customer Churn Analysis",
    labels={"x": "Customer Status", "y": "Count"}
)

st.plotly_chart(fig, use_container_width=True)

st.info("Customers with below-average spending are classified as 'At Risk'.")