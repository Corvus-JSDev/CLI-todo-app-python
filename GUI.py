from funcs.functions import *
import FreeSimpleGUI as sg

add_todo_label = sg.Text("Type in a ToDo:")
inputbox = sg.InputText(tooltip="Enter a ToDo:", key="todo")
add_button = sg.Button("Add")
quit_button = sg.Button("Quit")

window = sg.Window('My ToDo app',
			 layout=[
				 [add_todo_label],  # row 1
				 [inputbox, add_button],  # row 2
				 [quit_button]
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

	match event.lower():
		case "quit":
			break

		case "add":
			add_todo = value["todo"].strip().capitalize()

			todo_list = get_todo()
			todo_list.append(add_todo + "\n")

			write_todo(todo_list)
			print(f'\'{add_todo}\' has been added')

window.close()