# use (uv run streamlit run main.py) to run project
# Streamlit mainly declarative style mein UI banane deta hai, lekin Python code mein imperative logic bhi likh sakte ho.
# uv ek tool hai jo Python ke packages install karne aur Python projects manage karne ke kaam aata ha


import streamlit as st

st.title("Welcome to the Transcendent Realm")
st.subheader("This is the Transcendent Army")
st.text("This is ....")
st.write("Hello World!")

power = st.selectbox('Choose the God you want to serve:', ['The Sword God', 'The Death God', '  God of Light', 'The Dragon God'])
st.write(f'Your choice {power} is an excellent choice')

st.success('Your choice has been selected')

if st.button('Choose your weapon'):
  st.success('Your weapon has been selected')

selected_weapon = st.checkbox('Balmung - The DragonSlayer Sword')

if selected_weapon:
  st.write('Weapon has been selected')

skill_type = st.radio('Pick your class skill:', ['Enhancement', 'Mage', 'Swordmaster', 'Bererker', 'Necromancer', 'Ancient Runes Creator'])
st.write(f'Selected skill: {skill_type}')

mana = st.slider('Mana level', 100, 1000, 300)
st.write(f'Selected mana level {mana}')

max_skills = st.number_input('Max skills you can possess', min_value=1, max_value=5, step=1)
st.write(f'Selected skills: {max_skills}')


name = st.text_input('Enter your name')
if name:
  st.write(f'Welcome, {name} ! You are ready')

dob = st.datetime_input('Select your birth date')
st.write(f'Your dob is {dob}' )