import streamlit as st
import pandas as pd

st.title("Mi primer dashboard")

df = pd.read_csv("data/ventas.csv")
region = st.selectbox("Elige una region", sorted(df["region"].unique()))

df_filtrado = df[df["region"] == region]
st.metric("Ingreso total", f"${df_filtrado['ingreso'].sum():,.0f}")
st.dataframe(df_filtrado.head(20))
