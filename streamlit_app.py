import streamlit as st
import pandas
import requests
import st.connector

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
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)


st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)



