import streamlit as st
from funcs.functions import *


def add_todo():
	new_todo = str(st.session_state["new_todo_input"]).strip().capitalize()
	todo_list.append(new_todo + "\n")
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
	st.checkbox(todo, key=f'active_todo {todo_index}')
	todo_index += 1


# Complete todos
for todo in st.session_state:
	if todo.startswith("active_todo") and st.session_state[todo]:
		# Remove the todo from the txt file
		index = todo.split(" ")[1]
		todo_list.pop(int(index))
		write_todo(todo_list)

		# Update the session list and the on-screen todos
		del st.session_state[todo]
		st.rerun()



# print(st.session_state)