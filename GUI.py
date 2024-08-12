from funcs.functions import *
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("user_todo.txt"):
	with open("user_todo.txt", "w"):
		pass


# Remove the last 2 characters (\n) from each item
# todo_list = [item[:-1] for item in get_todo()]

# Find themes here: https://docs.pysimplegui.com/en/latest/documentation/module/themes/
sg.theme("DarkBlue14")

clock = sg.Text(time.strftime("%b %d, \'%y %I:%M %p"), key="clock")
add_todo_label = sg.Text("Type in a ToDo:")
inputbox = sg.InputText(tooltip="Enter a ToDo:", key="input_todo")
list_box = sg.Listbox(values=[item[:-1] for item in get_todo()], key='edit_todos', enable_events=True, size=(45, 10))
add_button = sg.Button("Add", tooltip="Add todo", mouseover_colors="LightBlue2")
edit_button = sg.Button("Edit", mouseover_colors="LightBlue2")
complete_button = sg.Button("Complete", mouseover_colors="LightBlue2")
quit_button = sg.Button("Quit")

window = sg.Window('My ToDo app',
			 layout=[
				 [clock],
				 [add_todo_label],  # row 1
				 [inputbox, add_button],  # row 2
				 [list_box, edit_button, complete_button],
				 [quit_button],
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

# Start the GUI
while True:
	event, value = window.read(timeout=50_000)  # update automatically every 50secs
	# print(f'event: {event}\nvalue: {value}\n')

	# Read event values
	match event:
		case "Quit" | sg.WIN_CLOSED:
			break

		case "Add":
			add_todo = value["input_todo"].strip().capitalize()
			if add_todo != "":
				todo_list = get_todo()
				todo_list.append(add_todo + "\n")
				write_todo(todo_list)

				window["edit_todos"].update(values=[item[:-1] for item in todo_list])
				window["input_todo"].update(value="")

		case "Edit":
			try:
				edit_choice = value["edit_todos"][0] + "\n"
				new_todo = str(value["input_todo"]).strip().capitalize() + "\n"
				todo_list = get_todo()
				index = todo_list.index(edit_choice)
				todo_list[index] = new_todo
				write_todo(todo_list)

				window["edit_todos"].update(values=[item[:-1] for item in todo_list])
			except IndexError:
				sg.popup("Please select a todo", font=("inter", 14))
		case "edit_todos":
			# This will update the input-box whenever the user clicks a todo inside the edit_todos box
			try:
				window['input_todo'].update(value=value["edit_todos"][0])
			except IndexError:
				print("IndexError: list index out of range")

		case "Complete":
			try:
				complete_choice = value["edit_todos"][0] + "\n"
				todo_list = get_todo()
				index = todo_list.index(complete_choice)
				todo_list.pop(index)
				write_todo(todo_list)

				# Update the list of todos and clear the input-box
				window["edit_todos"].update(values=[item[:-1] for item in todo_list])
				window['input_todo'].update(value="")
			except IndexError:
				sg.popup("Please select a todo", font=("inter", 14))

	window["clock"].update(value=time.strftime("%b %d, \'%y %I:%M %p"))

window.close()
