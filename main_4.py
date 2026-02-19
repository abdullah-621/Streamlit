import streamlit as st
import pandas as pd

st.title("File Uploder Dashboard")

file = st.file_uploader("Upload your csv files", type=['csv'])

if file:
  df = pd.read_csv(file)
  st.write(df)

if file:
  st.write(df.describe())
  st.dataframe(df.describe())