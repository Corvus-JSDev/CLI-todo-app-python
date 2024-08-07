completed_todos = 0

help_commands ="""
1) Add <todo>: Add a todo.
2) Show: Show all your todos.
3) Edit <number>: Edit a single todo.
4) Complete <number>: Select what todo you have completed.
5) Quit: Exit the program.
"""


print("type 'help' for a list of commands\n")
while True:
	user_command = input("\nWrite a command: ").lower().strip()

	if "help" in user_command:
		print(help_commands)

	if "add" in user_command:
		# .capitalize() will capitalize the first letter of the 'first' word
		# .strip() will remove any trailing or leading spaces
		add_todo = user_command.removeprefix("add").strip().capitalize() + "\n"

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

	if "show" in user_command:
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

	if "edit" in user_command:
		edit_choice = int(user_command.removeprefix("edit").strip())

		with open("user_todo.txt", "r") as file:
			todo_list = file.readlines()

		if edit_choice > len(todo_list) or edit_choice <= 0:
			print(f"That todo doesnt exist.")
		else:
			with open('user_todo.txt', 'w') as file:
				print(f'\nEditing: {todo_list[edit_choice - 1]}', end="")
				todo_list[edit_choice - 1] = input('New todo: ').capitalize() + "\n"
				file.writelines(todo_list)

	if "complete" in user_command:
		completed_choice = int(user_command.removeprefix("complete").strip())

		with open('user_todo.txt', 'r') as file:
			todo_list = file.readlines()

		if completed_choice > len(todo_list) or completed_choice <= 0:
			print(f"That todo doesnt exist.")
		else:
			with open('user_todo.txt', 'w') as file:
				todo_list.remove(todo_list[completed_choice - 1])
				file.writelines(todo_list)
				# completed_todos += 1
				print("Successfully completed a todo")

	if "quit" in user_command:
		break


print("\n\nYou have ended the program... goodbye")












