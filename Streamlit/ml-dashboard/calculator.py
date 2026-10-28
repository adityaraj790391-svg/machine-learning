import streamlit as st

st.title('My Calculator')
st.write('Perform Basic Mathematical Operations')

num1 = st.number_input('Enter your number', value=0.0)
num2 = st.number_input('Enter second number', value=0.0)

operation = st.selectbox(
  'Choose operation', ['Addition', 'Subtarction', 'Multiplication', 'Division']
)

if st.button