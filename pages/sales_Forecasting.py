import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Sales Forecast")
st.write("Page loaded successfully")

df = pd.read_csv("online_retail_cleaned_small.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head(20))
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Sales"] = df["Quantity"] * df["UnitPrice"]

monthly_sales = (
    df.groupby(df["InvoiceDate"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["InvoiceDate"] = monthly_sales["InvoiceDate"].astype(str)

# KPI Cards
total_sales = df['Sales'].sum()
total_orders = df['InvoiceNo'].nunique()
total_customers = df['CustomerID'].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Sales", f"${total_sales:,.0f}")

with col2:
    st.metric("📦 Total Orders", total_orders)

with col3:
    st.metric("👥 Total Customers", total_customers)

fig = px.line(
    monthly_sales,
    x="InvoiceDate",
    y="Sales",
    title="Historical Sales Trend"
)

st.plotly_chart(fig, use_container_width=True)

avg_sales = monthly_sales["Sales"].mean()

st.metric(
    "Expected Monthly Sales",
    f"${avg_sales:,.0f}"
)

st.metric(
    "Predicted Next Month Sales",
    f"${avg_sales:,.0f}"
)

st.info(
    "Forecast based on average historical monthly sales performance."
)

