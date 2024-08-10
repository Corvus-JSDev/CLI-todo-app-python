# from funcs.functions import remove_first_word, get_todo, write_todo
import FreeSimpleGUI as sg

add_todo_label = sg.Text("Type in a ToDo:")
inputbox = sg.InputText(tooltip="Enter a ToDo:", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My ToDo app',
			 layout=[
				 [add_todo_label],  # row 1
				 [inputbox, add_button]  # row 2
				 ],
			 font=("inter", 14))


"""
event = window.read()
print(event)        # ('Add', {'todo': 'hello world'})
print(event[0])     # Add
print(event[1])     # {'todo': 'hello world'}
print(event[1][0])  # hello world

event, value = window.read()
print(event)  # Add
print(value)  # {'todo': 'hello world'}
print(value["todo"])  # hello world
"""

while True:
	event, value = window.read()
	if value["todo"] == "quit":
		break
	else:
		print(event, value["todo"])

window.close()