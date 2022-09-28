import streamlit as st
import pandas as pd
import csv
import sys
import os

st.title('WINE!!!')
st.subheader('testing streamlit features')
st.image('https://images.ctfassets.net/8x8155mjsjdj/1af9dvSFEPGCzaKvs8XQ5O/a7d4adc8f9573183394ef2853afeb0b6/Copy_of_Red_Wine_Blog_Post_Header.png')

st.slider('HOW MUCH DO YOU ENJOY WINE?', min_value=0, max_value=10)
st.date_input('Your birthday')

df = pd.read_csv('winemag-data_first150k.csv', usecols = ['country','points','price'])

st.code('for i in range(8): foo()')

st.info('Red wine best wine')

st.dataframe(df)

with st.sidebar:
   st.radio('Select one:', ['Red Wines', 'White Wines'])

df_us = pd.DataFrame()

i_pos = 0

for i in df.iloc[:, 0]:
    if (isinstance(i, str)):
        if (i.__contains__("US") == True):
            df_us_newrow = pd.DataFrame({
                'country' : [df.iloc[i_pos]['country']],
                'points' : [df.iloc[i_pos]['points']],
                'price' : [df.iloc[i_pos]['price']],
            })
            df_us = pd.concat([df_us, df_us_newrow], ignore_index=True)
    i_pos += 1
st.dataframe(df_us)
print(df_us) #to the terminal