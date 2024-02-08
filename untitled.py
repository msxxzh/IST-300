import streamlit as st
python -m pip install -U pip
python -m pip install -U matplotlib
import matplotlib.pyplot as plt
import numpy as np
st.write('Hello World')
if st.checkbox('agree') == True:
  st.write ('Congratulations')
  st.balloons()
