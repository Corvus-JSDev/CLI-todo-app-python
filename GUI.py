from funcs.functions import *
import FreeSimpleGUI as sg

# Remove the last 2 characters (\n) from each item
# todo_list = [item[:-1] for item in get_todo()]

add_todo_label = sg.Text("Type in a ToDo:")
inputbox = sg.InputText(tooltip="Enter a ToDo:", key="todo")
list_box = sg.Listbox(values=[item[:-1] for item in get_todo()], key='edit_todos', enable_events=True, size=(45, 10))
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
quit_button = sg.Button("Quit")

window = sg.Window('My ToDo app',
			 layout=[
				 [add_todo_label],  # row 1
				 [inputbox, add_button],  # row 2
				 [list_box, edit_button],
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
	# Start the GUI
	event, value = window.read()

	# Read input values
	match event:
		case "Quit" | sg.WIN_CLOSED:
			break

		case "Add":
			add_todo = value["todo"].strip().capitalize()

			todo_list = get_todo()
			todo_list.append(add_todo + "\n")

			write_todo(todo_list)
			print(f'\'{add_todo}\' has been added')

		case "Edit":
			edit_choice = value["edit_todos"][0] + "\n"
			new_todo = str(value["todo"]).strip() + "\n"
			todo_list = get_todo()
			index = todo_list.index(edit_choice)
			todo_list[index] = new_todo
			write_todo(todo_list)




window.close()
