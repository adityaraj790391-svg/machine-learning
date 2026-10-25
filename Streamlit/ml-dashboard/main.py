# use (uv run streamlit run main.py) to run project
# Streamlit mainly declarative style mein UI banane deta hai, lekin Python code mein imperative logic bhi likh sakte ho.
# uv ek tool hai jo Python ke packages install karne aur Python projects manage karne ke kaam aata ha


import streamlit as st

st.title("My First Streamlit App")
st.subheader("A simple Streamlit application")
st.text("This is a simple Streamlit application.")
st.write("Hello World!")


