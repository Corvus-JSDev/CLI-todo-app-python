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


todo_save_file = "user_todo.txt"
def get_todo(file_path):
	# Context Managers are important to use because they not only take up less lines of code, but they will also use context to close any opened files if an errors are thrown
	with open(file_path, 'r') as text_file:
		text = text_file.readlines()
	return text


def write_todo(filepath, todo):
	with open(filepath, 'w') as text_file:
		text_file.writelines(todo)


while True:
	user_command = input("\nWrite a command: ").lower().strip()

	#* HELP
	if user_command.startswith("help") or user_command.startswith("h"):
		print(help_commands)

	#* ADD
	elif user_command.startswith('add') or user_command.startswith('a'):
		# .capitalize() will capitalize the first letter of the 'first' word
		# .strip() will remove any trailing or leading spaces
		add_todo = remove_first_word(user_command).strip().capitalize()

		# Open the txt file and output its contents into the todo_list
		todo_list = get_todo(todo_save_file)
		todo_list.append(add_todo + "\n")

		# Write (w) the contents of todo_list to the txt file
		# The files will update when the program is ended
		# Note: w will over-write the entire file
		write_todo(todo_save_file, todo_list)
		print(f'\'{add_todo}\' has been added')

	#* SHOW
	elif user_command.startswith("show") or user_command.startswith("s"):
		todo_list = get_todo(todo_save_file)

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
			todo_list = get_todo(todo_save_file)

			if edit_choice > len(todo_list) or edit_choice <= 0:
				print(f"That todo doesnt exist.")
			else:
				print(f'\nEditing: {todo_list[edit_choice - 1]}', end="")
				todo_list[edit_choice - 1] = input('New todo: ').capitalize() + "\n"
				write_todo(todo_save_file, todo_list)
		except ValueError:
			print(f'\'{edit_choice}\' is not a valid option. Please input a single number.\ne.g. \'edit 3\'')
			continue

	#* COMPLETE
	elif user_command.startswith("complete") or user_command.startswith('c'):
		completed_choice = remove_first_word(user_command).strip()

		try:
			# completed_choice = completed_choice.split()
			indices = [ int(num) for num in completed_choice.split() ]
			indices.sort(reverse=True)
			todo_list = get_todo(todo_save_file)

			index = 0
			for num in indices:
				if num > len(todo_list) or num <= 0:
					print(f"{num} todo does not exist.")
				else:
					todo_list.pop(num - 1)
					index += 1

			write_todo(todo_save_file, todo_list)
			print(f"Successfully completed {index} {'todos' if index > 1 else 'todo'}.")
		except ValueError:
			print(f'Error: That is not a valid option. Please only input numbers separated by spaces.\ne.g. \'complete 1 2 3\'')

	#* QUIT
	elif user_command.startswith('quit') or user_command.startswith('q'):
		print("\n\nYou have ended the program... goodbye")
		quit()

	else:
		print(f'\'{user_command}\' is not a valid command. Type \'help\' for a list of commands')
