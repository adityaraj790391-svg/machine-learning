import streamlit as st
import pandas as pd

st.title('Class Selection Poll')

file = st.file_uploader('Upload your CSV file', type = ['csv'])

if file:
  df = pd.read_csv(file)
  st.subheader('Data Preview')
  st.dataframe(df)

if file:
  st.subheader('Summary Stats')
  st.write(df.describe())

  

