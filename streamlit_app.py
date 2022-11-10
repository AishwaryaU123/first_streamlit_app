import streamlit
streamlit.title('My parents Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Idli Sambar')
streamlit.text('🍞 Masala Dosa')
streamlit.text(' 🥗 Uttappam')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
