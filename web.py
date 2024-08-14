import streamlit as st
from funcs.functions import *


def add_todo():
	new_todo = str(st.session_state["new_todo_input"]).strip().capitalize() + "\n"
	todo_list.append(new_todo)
	write_todo(todo_list)
	st.session_state["new_todo_input"] = ""
	print(f'\'{new_todo}\' has been added.')


st.title('My todo app')
st.subheader('This is a simple todo app')
st.write('meant to increase productivity')

st.text_input(label='Enter a ToDo:', placeholder="Cook dinner", on_change=add_todo, key="new_todo_input")

# Add the todos to the page
todo_list = get_todo()
todo_index = 0
for todo in todo_list:
	st.checkbox(todo, key=todo_index)
	todo_index += 1


# st.session_state