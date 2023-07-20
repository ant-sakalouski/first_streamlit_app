import streamlit
import pandas

streamlit.title("Hello, snowflake")
streamlit.header("My header")
streamlit.text("Sample text")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)