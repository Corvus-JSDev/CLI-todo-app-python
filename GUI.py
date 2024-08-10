# from funcs.functions import remove_first_word, get_todo, write_todo
import FreeSimpleGUI as sg

add_todo_label = sg.Text("Type in a ToDo:")
inputbox = sg.InputText(tooltip="Enter a ToDo:")
add_button = sg.Button("Add")

window = sg.Window('My ToDo app',
			 layout=[
				 [add_todo_label],  # row 1
				 [inputbox, add_button]  # row 2
				 ],
			 font=("inter", 14))

window.read()
window.close()