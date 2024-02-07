import streamlit as st

st.write('Hello World')
if st.checkbox('agree') == True:
  st.write ('Congratulations')
  st.balloons()
