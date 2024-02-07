import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.write('Hello World')
if st.checkbox('agree') == True:
  st.write ('Congratulations')
  st.balloons()
