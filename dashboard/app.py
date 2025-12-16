import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv("data/processed/processed.csv")
model = joblib.load("models/model.joblib")

st.title("Soil Moisture Monitoring")

latest = df.iloc[-1]
X = latest[["moisture0","moisture1","moisture2","moisture3","hour"]].to_frame().T
pred = model.predict(X)[0]

if pred == 1:
    st.error("WATER NOW")
else:
    st.success("NO WATER NEEDED")

df_plot = df.tail(5000).copy()
df_plot["timestamp"] = pd.to_datetime(df_plot["timestamp"])
df_plot = df_plot.set_index("timestamp")

st.line_chart(df_plot[["moisture0","moisture1","moisture2","moisture3"]])

