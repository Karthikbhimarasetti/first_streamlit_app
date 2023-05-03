import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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


def get_fruityvice_data(this_fruit_choice):
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized



st.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
      st.error("Please select a fruit to get information")
    else:
      back_from_function=get_fruityvice_data(fruit_choice)
      st.dataframe(back_from_function)

except URLError as e:
  st.error()
  
#st.write('The user entered ', fruit_choice)



#st.stop()


# my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# st.header("the fruit load list contains: ")
# st.dataframe(my_data_row)


st.header("the fruit load list contains: ")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
    
if st.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    st.dataframe(my_data_rows)



add_my_fruit=st.text_input("What fruit would you like to add?","jackfruit")
st.write("Thanks for adding "+add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")


def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding "+new_fruit
        
add_my_fruit=st.text_input('What fruit would you like to add?')
if st.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    back_from_function= insert_row_snowflake(add_my_fruit)
    st.text(back_from_function)
