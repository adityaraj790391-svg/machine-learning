import streamlit as st

st.title('Class Selection Poll')

col1, col2 = st.columns(2)

with col1:
  st.header('Barrier Master')
  vote1 = st.button('Select Barrier Master')


with col2:
  st.header('Sword Master')
  vote2 = st.button('Select Sword Master')

if vote1:
  st.success('Your class is Barrier Master')
elif vote2:
  st.success('Your class is Sword Master')

