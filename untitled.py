import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write('Hello World')
if st.checkbox('yes') == True:
  st.balloons()
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
st.progress(10)
st.sidebar.title("Sidebar")

df = pd.DataFrame(   
    np.random.randn(500, 3),   
    columns=['x','y','z'])

c =alt.Chart(df).mark_circle().encode(   
    x='x' , y='y' , size='z', color='z', tooltip ['x', 'y', 'z'])

st.altair_chart(c, use_container_width=True)

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(df)
