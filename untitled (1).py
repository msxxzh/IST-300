import streamlit as st
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
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])s
t.slider('Pick a number', 0,50)

st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):    time.sleep(10)


rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df= pd.DataFrame(
    np.random.randn(10, 2), 
    columns=['x', 'y'])
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)


df = pd.DataFrame(   
    np.random.randn(500, 3),   
    columns=['x','y','z'])

c =alt.Chart(df).mark_circle().encode(   
    x='x' , 'y'=y , size='z', color='z', tooltip ['x', 'y', 'z'])

st.altair_chart(c, use_container_width=True)

st.graphviz_chart('''
    digraph {
    Big_shark -> Tuna
    Tuna -> Mackerel
    Mackerel -> Small_fishes
    Small_fishes -> Shrimp
    }
''')

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(df)