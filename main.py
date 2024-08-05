todo_list = []

help_commands ="""
1) Add: Add a todo.
2) Show: Show all your todos.
3) Edit: Edit a single todo.
4) Quit: Exit the program.
"""


print("type 'help' for a list of commands\n")
while True:
	user_command = input("Write a command: ").lower()

	match user_command:
		case "help" | "h":
			print(help_commands)

		case "add" | "a":
			# .title() will capitalize the first letter of 'every' word.
			# .capitalize() will capitalize the first letter of the 'first' word
			# .strip() will remove any trailing or leading spaces
			todo = input("Enter a todo: ").capitalize().strip()
			todo_list.append(todo)

		case "show" | "display" | "s":
			index = 0
			for item in todo_list:
				index += 1
				print(f"{index}. {item}")

		case "edit" | "e":
			edit_choice = int(input(f'Choose a todo to edit (1 ... {len(todo_list)}): '))
			if edit_choice > len(todo_list) or edit_choice <= 0:
				print(f"That todo doesnt exist.")
			else:
				print(f'Editing: {todo_list[edit_choice - 1]}')
				todo_list[edit_choice - 1] = input('New todo: ')

		case "quit" | "q":
			break

		case _:
			print(f'"{user_command}" is not a command.')

print("\n\nYou have ended the program... goodbye")












