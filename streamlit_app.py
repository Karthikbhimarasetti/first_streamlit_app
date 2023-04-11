import streamlit as st
import pandas

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.title('My Parents New Healthy Diner') 
st.header('Breakfast Menu')
st.text('🥣 Omega 3 and blueberry oatmeal')
st.text('🥗 Kale, Spinach & rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])

# Display the table on the page.
st.dataframe(my_fruit_list) 

