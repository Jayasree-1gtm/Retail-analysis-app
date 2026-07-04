import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RetailPulse Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("📊 RetailPulse")
st.sidebar.markdown("### Business Intelligence Suite")
st.sidebar.markdown("---")

df = pd.read_csv("online_retail_cleaned_small.csv")

df["Sales"] = df["Quantity"] * df["UnitPrice"]

st.title("📊 RetailPulse Analytics Dashboard")
st.caption("Business Intelligence Platform for Retail Performance Monitoring")

st.markdown("""
Retail Sales Analytics and Business Intelligence platform for monitoring sales performance, customer insights, inventory analysis, and forecasting.
""")
st .subheader("Key performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Orders", df["InvoiceNo"].nunique())
col3.metric("Customers", df["CustomerID"].nunique())
col4.metric("Products Sold", int(df["Quantity"].sum()))

st.subheader("Dataset Preview")
st.dataframe(df.head())

import plotly.express as px

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

monthly_sales = (
    df.groupby(df["InvoiceDate"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["InvoiceDate"] = monthly_sales["InvoiceDate"].astype(str)

fig = px.line(
    monthly_sales,
    x="InvoiceDate",
    y="Sales",
    title="Monthly Sales Trend"
)

st.plotly_chart(fig, use_container_width=True)

top_products = (
    df.groupby("Description")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig2 = px.bar(
    x=top_products.values,
    y=top_products.index,
    orientation="h",
    title="Top 10 Products by Sales"
)

st.plotly_chart(fig2, use_container_width=True)

country_sales = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig3 = px.pie(
    values=country_sales.values,
    names=country_sales.index,
    title="Sales by Country"
)

st.plotly_chart(fig3, use_container_width=True)

country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].dropna().unique().tolist())
)

if country != "All":
    df = df[df["Country"] == country]

    st.markdown("---")
st.markdown(
    "© 2026 RetailPulse Analytics | Developed using Python, Streamlit, Pandas and Plotly"
)

st.subheader("🌍 Top 10 Countries by Sales")

top_countries = (
    df.groupby("Country")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

fig = px.bar(
    x=top_countries.values,
    y=top_countries.index,
    orientation="h",
    title="Top 10 Countries by Sales"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption(
    "RetailPulse Analytics Dashboard | Built with Python, Streamlit, Pandas and Plotly"
)
