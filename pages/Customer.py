import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👥 Customer Analytics")

df = pd.read_csv("online_retail_cleaned_small.csv")
st.write("Rows:", len(df))
st.write(df.head())

df["Sales"] = df["Quantity"] * df["UnitPrice"]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "Sales": "sum"
}).reset_index()

rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]
# KPI Cards
col1, col2 = st.columns(2)

col1.metric("Total Customers", df["CustomerID"].nunique())
col2.metric("Countries", df["Country"].nunique())
fig = px.scatter(
    rfm,
    x="Frequency",
    y="Monetary",
    size="Monetary",
    color="Recency",
    hover_data=["CustomerID"],
    title="RFM Customer Analysis"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("RFM Customer Table")
st.dataframe(rfm)


