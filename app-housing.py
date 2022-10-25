import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

st.title('California Housing Data (1990) by Yuxuan Xu')
df = pd.read_csv('housing.csv')
price_fliter = st.slider('Median House Price', 0 , 500001 , 200000)

location_type_fliter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique())

incomelevel_fliter = st.sidebar.radio('Choose income level',('Low','Medium','High'))

df = df[df.median_house_value >= price_fliter]

df = df[df.ocean_proximity.isin(location_type_fliter)]

if incomelevel_fliter == 'Low':
    df = df[df.median_income <= 2.5]
elif incomelevel_fliter == 'Medium':
    df = df[(df.median_income> 2.5) & (df.median_income< 4.5)]
elif incomelevel_fliter == 'High':
    df = df[df.median_income >= 4.5]


st.subheader('See more fliters in the sidebar:')
st.map(df)
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize = (10,10))
val = df.median_house_value.hist(bins=30)
st.pyplot(fig)


