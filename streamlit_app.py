#import streamlit

streamlit.title('Just startede with GitHub & Streamlit!')

streamlit.header('Going with the Badge code for practice! Menu Card it is!')
streamlit.text('🥣Aloo Paratha')
streamlit.text('🥗Gobi Paratha')
streamlit.text('🐔Chicken Sandwitch')
streamlit.text('🐔Chicken Soup')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


# new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

# don't run the above part as we're working on fixing it.
streamlit.stop()


import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error impoer URLError

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_rows)

# new section to display fruityvice api response
streamlit.header("Fruit Advice!")
add_my_fruit = streamlit.text_input('What fruit would you like information about?','apple')
streamlit.write('The user entered ', add_my_fruit)

# this is for testing purpose, may be work may be not. Lets find out!
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
