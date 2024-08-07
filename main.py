completed_todos = 0

help_commands ="""
1) Add: Add a todo.
2) Show: Show all your todos.
3) Edit: Edit a single todo.
4) Complete: Select what todo you have completed.
5) Quit: Exit the program.
"""


print("type 'help' for a list of commands\n")
while True:
	user_command = input("\nWrite a command: ").lower()

	match user_command:
		case "help" | "h":
			print(help_commands)

		case "add" | "a":
			# .capitalize() will capitalize the first letter of the 'first' word
			# .strip() will remove any trailing or leading spaces
			add_todo = input("Enter a todo: ").capitalize().strip() + "\n"

			# Open the txt file and output its contents into the todo_list
			# file.readlineS() will return a list with each line in the file being a new item
			with open("user_todo.txt", "r") as file:
				todo_list = file.readlines()
				todo_list.append(add_todo)

			# Write (w) the contents of todo_list to the txt file
			# The files will update when the program is ended
			# Note: w will over-write the entire file
			with open('user_todo.txt', 'w') as file:
				file.writelines(todo_list)

		case "show" | "display" | "s":
			# Context Managers are important to use because they not only take up less lines of code, but they will also use context to close any opened files if an errors are thrown
			with open("user_todo.txt", "r") as file:
				todo_list = file.readlines()

			# print(f"\nYou have completed {completed_todos} tasks.")
			print("\n------- TODOs -------")
			if len(todo_list) == 0:
				print("There are currently no todos")
			else:
				for index, item in enumerate(todo_list):
					print(f"{index + 1}. {item}", end="")

		case "edit" | "e":
			with open("user_todo.txt", "r") as file:
				todo_list = file.readlines()

			edit_choice = int(input(f'Choose a todo to edit (1 ... {len(todo_list)}): '))
			if edit_choice > len(todo_list) or edit_choice <= 0:
				print(f"That todo doesnt exist.")
			else:
				with open('user_todo.txt', 'w') as file:
					print(f'\nEditing: {todo_list[edit_choice - 1]}', end="")
					todo_list[edit_choice - 1] = input('New todo: ').capitalize() + "\n"
					file.writelines(todo_list)

		case "complete" | "c":
			with open('user_todo.txt', 'r') as file:
				todo_list = file.readlines()

			completed_choice = int(input(f'Choose the todo you have finished (1 ... {len(todo_list)}): '))
			if completed_choice > len(todo_list) or completed_choice <= 0:
				print(f"That todo doesnt exist.")
			else:
				with open('user_todo.txt', 'w') as file:
					todo_list.remove(todo_list[completed_choice - 1])
					file.writelines(todo_list)
					# completed_todos += 1
					print("Successfully completed a todo")

		case "quit" | "q":
			break

		case _:
			print(f'"{user_command}" is not a command.')

print("\n\nYou have ended the program... goodbye")












