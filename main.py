#    <dir>.<file name>      <functions 1>, <functions 2>, <functions 3>
from funcs.functions import remove_first_word, get_todo, write_todo
import time

current_day = time.strftime("%b %d, \'%y")
current_time = time.strftime("%I:%M %p")

print(f'Date: {current_day}')
print(f'Time: {current_time}')
print("\nType 'help' for a list of commands")

help_commands ="""
1) Add <todo> .......... Add a todo.
2) Show ................ Show all your todos.
3) Edit <number> ....... Edit a single todo.
4) Complete <number> ... Select what todo you have completed.
5) Quit ................ End the program.
"""


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
		todo_list = get_todo()
		todo_list.append(add_todo + "\n")

		# Write (w) the contents of todo_list to the txt file
		# The files will update when the program is ended
		# Note: w will over-write the entire file
		write_todo(todo_list)
		print(f'\'{add_todo}\' has been added')

	#* SHOW
	elif user_command.startswith("show") or user_command.startswith("s"):
		todo_list = get_todo()

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
			todo_list = get_todo()

			if edit_choice > len(todo_list) or edit_choice <= 0:
				print(f"That todo doesnt exist.")
			else:
				print(f'\nEditing: {todo_list[edit_choice - 1]}', end="")
				todo_list[edit_choice - 1] = input('New todo: ').capitalize() + "\n"
				write_todo(todo_list)
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
			todo_list = get_todo()

			index = 0
			for num in indices:
				if num > len(todo_list) or num <= 0:
					print(f"{num} todo does not exist.")
				else:
					todo_list.pop(num - 1)
					index += 1

			write_todo(todo_list)
			print(f"Successfully completed {index} {'todos' if index > 1 else 'todo'}.")
		except ValueError:
			print(f'Error: That is not a valid option. Please only input numbers separated by spaces.\ne.g. \'complete 1 2 3\'')

	#* QUIT
	elif user_command.startswith('quit') or user_command.startswith('q'):
		print("\n\nYou have ended the program... goodbye")
		quit()

	else:
		print(f'\'{user_command}\' is not a valid command. Type \'help\' for a list of commands')
