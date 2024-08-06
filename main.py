completed_todos = 0

help_commands ="""
! 1) Add: Add a todo.
* 2) Show: Show all your todos.
? 3) Edit: Edit a single todo.
TODO: 4) Complete: Select what todo you have completed.
5) Quit: Exit the program.

"""


print("type 'help' for a list of commands\n")
while True:
	user_command = input("Write a command: ").lower()

	match user_command:
		case "help" | "h":
			print(help_commands)

		case "add" | "a":
			# .capitalize() will capitalize the first letter of the 'first' word
			# .strip() will remove any trailing or leading spaces
			add_todo = input("Enter a todo: ").capitalize().strip() + "\n"

			# Open the txt file and output its contents into the todo_list
			# file.readlineS() will return a list with each line in the file being a new item
			# file.readline() (with NO s) will only read a single line and return a string
			file = open("user_todo.txt", "r")
			todo_list = file.readlines()
			todo_list.append(add_todo)
			# It's important to close the file once you're done with it because other lines in the program may			interact with it, if it's still open
			file.close()

			# Write (w) the contents of todo_list to the txt file
			# The files will update when the program is ended
			# Note: w will over-write the entire file
			file = open('user_todo.txt', 'w')
			file.writelines(todo_list)
			file.close()

		case "show" | "display" | "s":
			file = open("user_todo.txt", "r")
			todo_list = file.readlines()
			file.close()  # closing a file will not affect the contents of todo_list

			index = 0
			print(f"You have completed {completed_todos} tasks.")
			if len(todo_list) == 0:
				print("There are currently no todos")
			else:
				for item in todo_list:
					index += 1
					print(f"{index}. {item}", end="")

		case "edit" | "e":
			edit_choice = int(input(f'Choose a todo to edit (1 ... {len(todo_list)}): '))
			if edit_choice > len(todo_list) or edit_choice <= 0:
				print(f"That todo doesnt exist.")
			else:
				print(f'Editing: {todo_list[edit_choice - 1]}')
				todo_list[edit_choice - 1] = input('New todo: ').capitalize()

		case "complete" | "c":
			completed_choice = int(input(f'Choose the todo you have finished (1 ... {len(todo_list)}): '))
			if completed_choice > len(todo_list) or completed_choice <= 0:
				print(f"That todo doesnt exist.")
			else:
				todo_list.remove(todo_list[completed_choice - 1])
				print("Successfully completed a todo")
				completed_todos += 1

		case "quit" | "q":
			break

		case _:
			print(f'"{user_command}" is not a command.')

print("\n\nYou have ended the program... goodbye")












