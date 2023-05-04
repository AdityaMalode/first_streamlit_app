import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

#first paragraph of menu and all.
streamlit.title('Just startede with GitHub & Streamlit!')

streamlit.header('Going with the Badge code for practice! Menu Card it is!')
streamlit.text('🥣Aloo Paratha')
streamlit.text('🥗Gobi Paratha')
streamlit.text('🐔Chicken Sandwitch')
streamlit.text('🐔Chicken Soup')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# create a response code block(called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?',)
  if not fruit_choice:
      streamlit.error("Please select a fruit to get an information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

  
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The Fruit load list contains:")
#streamlit.dataframe(my_data_rows)

streamlit.header("The Fruit load list contains:")
#snowflake related function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
  
# add a bottom to load a fruit
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
 
# allow end user to add new fruit
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
      my_cur.execute("Insert into fruit load list values ('from streamlit')")
      return "Thanks for adding" + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add fruit to a list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
  


# new section to display fruityvice api response
#streamlit.header("Fruit Advice!")
#add_my_fruit = streamlit.text_input('What fruit would you like information about?','apple')
#streamlit.write('The user entered ', add_my_fruit)

# this is for testing purpose, may be work may be not. Lets find out!
#my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")


#import streamlit







# Display the table on the page.
#streamlit.dataframe(fruits_to_show)



    
#streamlit.write('The user entered ', fruit_choice)



# don't run the above part as we're working on fixing it.
streamlit.stop()



