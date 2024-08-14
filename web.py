import streamlit as st
from funcs.functions import *

st.title('My todo app')
st.subheader('This is a simple todo app')
st.write('meant to increase productivity')

st.text_input(label='Enter a ToDo:', placeholder="Cook dinner")

# Add the todos to the page
todo_list = get_todo()
for todo in todo_list:
	st.checkbox(todo)
