import streamlit as st

st.title('Class Selection Poll')

col1, col2 = st.columns(2)

with col1:
  st.header('Barrier Master')
  vote1 = st.button('Select Barrier Master')
  st.image('https://imgs.search.brave.com/WKwKF4qVuBrPxIQ5p1Oo1PG6tKL1QVmpp_gLX2A5yrs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzL2U3L2Fj/L2ZlL2U3YWNmZWYw/ODc3NjhhY2I1YjZk/NDYyZGQwNGJkNGVm/LmpwZw', width = 230)


with col2:
  st.header('Sword Master')
  vote2 = st.button('Select Sword Master')
  st.image('https://imgs.search.brave.com/O8NjeVixgofPdT7G8PROBDsUOMLJPp9KFMjZO-l4cMc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zd29y/ZG1hc3RlcnN5b3Vu/Z2VzdHNvbi5jbHVi/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDI0/LzExL1N3b3JkbWFz/dGVycy1Zb3VuZ2Vz/dC1Tb24ud2VicA', width = 220)

if vote1:
  st.success('Your class is Barrier Master')
elif vote2:
  st.success('Your class is Sword Master')


name = st.sidebar.text_input('Enter name')
skill = st.sidebar.selectbox('Activating Divine Exclusive Skill', ['Revelation of the Worlds Creation', 'Saintess of a Fallen Nation', 'King of Tyranny'])


