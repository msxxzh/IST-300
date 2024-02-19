import streamlit as st
pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import graphviz as graphviz

st.write('Hello World')
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
