import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👥 Customer Analytics")

df = pd.read_csv("online_retail_cleaned_small.csv")
st.write("Rows:", len(df))
st.write(df.head())

df["Sales"] = df["Quantity"] * df["UnitPrice"]

customer_sales = (
    df.groupby("CustomerID")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
fig = px.scatter(
    customer_ci,
    x="CustomerID",
    y="Customer_Index",
    title="Customer CI Dashboard"
)

st.plotly_chart(fig, use_container_width=True)

# KPI Cards
col1, col2 = st.columns(2)

col1.metric("Total Customers", df["CustomerID"].nunique())
col2.metric("Countries", df["Country"].nunique())

# Customer Distribution by Country
top_countries = df.groupby('Country')['CustomerID'].nunique().sort_values(ascending=False).head(10)

fig = px.bar(
    x=top_countries.index,
    y=top_countries.values,
    labels={'x':'Country','y':'Customers'},
    title='Top 10 Countries by Customers'
)

st.plotly_chart(fig, use_container_width=True)
