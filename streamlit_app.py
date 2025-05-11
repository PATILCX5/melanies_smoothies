# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customise Your Smoothie :cup_with_straw:")
st.write(
  """Choose the fruits you want in custom Smoothie!
  """)

title = st.text_input("Name on Smoothie:")
st.write("Name on your Smoothie will be:", title)

cnx = st.connection("Snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    "Choose upto 5 ingredients: ",
    my_dataframe,
    max_selections=5
)
if ingredients_list:
    

    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen +' '


    #st.write(ingredients_string)

    NAME_ON_ORDER = title
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, NAME_ON_ORDER)
            values ('""" + ingredients_string + """','"""+NAME_ON_ORDER+"""')"""

    #st.write(my_insert_stmt)
    #st.stop()
    time_to_insert =  st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success(f'Your Smoothie is ordered! {NAME_ON_ORDER}', icon="✅")

import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
#st.text(smoothiefroot_responce.json())
sf_df = dataframe(data=smoothiefroot_responce.json(),use_container_width = True)
