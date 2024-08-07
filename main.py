print("type 'help' for a list of commands\n")

help_commands ="""
1) Add <todo> .......... Add a todo.
2) Show ................ Show all your todos.
3) Edit <number> ....... Edit a single todo.
4) Complete <number> ... Select what todo you have completed.
5) Quit ................ End the program.
"""

def remove_first_word(s):
	words = s.split()
	if len(words) > 1:
		return ' '.join(words[1:])
	return ''

while True:
	user_command = input("\nWrite a command: ").lower().strip()

	#* HELP
	if user_command.startswith("help") or user_command.startswith("h"):
		print(help_commands)

	#* ADD
	elif user_command.startswith('add') or user_command.startswith('a'):
		# .capitalize() will capitalize the first letter of the 'first' word
		# .strip() will remove any trailing or leading spaces
		add_todo = remove_first_word(user_command).strip().capitalize() + "\n"

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

	#* SHOW
	elif user_command.startswith("show") or user_command.startswith("s"):
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

	#* EDIT
	elif user_command.startswith('edit') or user_command.startswith('e'):
		edit_choice = remove_first_word(user_command).strip()

		try:
			edit_choice = int(edit_choice)
			with open("user_todo.txt", "r") as file:
				todo_list = file.readlines()

			if edit_choice > len(todo_list) or edit_choice <= 0:
				print(f"That todo doesnt exist.")
			else:
				with open('user_todo.txt', 'w') as file:
					print(f'\nEditing: {todo_list[edit_choice - 1]}', end="")
					todo_list[edit_choice - 1] = input('New todo: ').capitalize() + "\n"
					file.writelines(todo_list)
		except ValueError:
			print(f'\'{edit_choice}\' is not a valid option. Please input a single number.\ne.g. \'edit 3\'')
			continue

	#* COMPLETE
	elif user_command.startswith("complete") or user_command.startswith('c'):
		completed_choice = remove_first_word(user_command).strip()

		try:
			completed_choice = completed_choice.split()

			with open('user_todo.txt', 'r') as file:
				todo_list = file.readlines()

			for num in completed_choice:
				num = int(num)
				if num > len(todo_list) or num <= 0:
					print(f"{num} todo does not exist.")
				else:
					with open('user_todo.txt', 'w') as file:
						todo_list.remove(todo_list[num - 1])
						file.writelines(todo_list)
						print("Successfully completed a todo")
		except ValueError:
			print(f'Error: That is not a valid option. Please only input numbers separated by spaces.\ne.g. \'complete 1 2 3\'')

	#* QUIT
	elif user_command.startswith('quit') or user_command.startswith('q'):
		break

	else:
		print(f'\'{user_command}\' is not a valid command. Type \'help\' for a list of commands')

print("\n\nYou have ended the program... goodbye")












